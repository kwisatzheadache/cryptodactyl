import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

seed = 7
numpy.random.seed(seed)

cols = array(merged.columns)[1:]
Y_partial = array(btc_up[:300])
X_partial = array(merged[:][:300])

Y = array(btc_up)
X = array(merged[cols][1:])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

btc_up = []
lookback = lag(merged['btcClose'], 1)

for i in range(len(lookback)):
    if lookback['btcClose'].iloc[i] < lookback['btcClose t - 1'].iloc[i]:
        btc_up.append(0)
    else:
        btc_up.append(1)

def baseline():
    model = Sequential()
    model.add(Dense(60, input_dim=42, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimator = KerasClassifier(build_fn=baseline, nb_epoch=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print(results.mean()*100, results.std()*100)
