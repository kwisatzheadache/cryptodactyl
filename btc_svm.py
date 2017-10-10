from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from numpy  import array
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


execfile('import.py')

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
X_partial = array(merged[:][:300])

Y = array(btc_up)
X = array(merged[cols][1:])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


model = SVC()
kfold = KFold(n_splits=6, random_state=7)
cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
print(cv_results.mean(), cv_results.std())

model.fit(X_train, Y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

print('Predictions for given dates:', predictions)
