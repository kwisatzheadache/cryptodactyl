from matplotlib import pyplot
from keras.models import Sequential
from keras import models
from keras import layers
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
from scipy.stats.stats import pearsonr
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from statsmodels.tsa.seasonal import seasonal_decompose
from numpy import array
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

btc_up = []
lookback = lag(merged['btcClose'], 1)

for i in range(len(lookback)):
    if lookback['btcClose'].iloc[i] < lookback['btcClose t - 1'].iloc[i]:
        btc_up.append(0)
    else:
        btc_up.append(1)

        test_size = .33
seed = 7
cols = array(merged.columns)[1:]
Y_partial = array(btc_up[:300])
X_partial = array(merged[cols][:300])

Y = array(btc_up)
X = array(merged[cols][1:])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

model = LogisticRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
print(accuracy_score(Y_test, predictions))

# Alternate model - 32-32-1, does not perform as well.
# model = Sequential()
# model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
# model.add(layers.Dense(1))
# model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

# model.fit(X_train, Y_train, epochs=5, batch_size=1)
# model.fit(X, Y, epochs=5, batch_size=1)
# ml5_mse, ml5_mae = model.evaluate(X_test, Y_test)

# # model.fit(X_train, Y_train, epochs=20, batch_size=1)
# # ml20_mse, ml20_mae = model.evaluate(X_test, Y_test)

# # comparison = [['persistence', persist_mae, persist_mse], ['ml5', ml5_mse, ml5_mae], ['ml20', ml20_mse, ml20_mae]]

# # print(comparison)

# Check out the GaussianNB stuff for classification predictions, and page 84 of brownlee ml learning

# models = []
# models.append(('LR', LogisticRegression()))
# models.append(('CART', DecisionTreeClassifier()))
# models.append(('NB', GaussianNB()))
# models.append(('SVM', SVC()))
# results = []
# names = []
# scoring = 'accuracy'

# for name, model in models:
#     kfold = KFold(n_splits=10, random_state=7)
#     cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)

# fig = pyplot.figure()
# fig.suptitle('algorithm comparison')
# ax = fig.add_subplot(111)
# pyplot.boxplot(results)
# ax.set_xticklabels(names)
# pyplot.show
