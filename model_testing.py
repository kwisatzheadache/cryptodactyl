# ----------------BEGIN MODEL TESTING -------------- #
cols = array(merged.columns)[1:]
X = array(merged[cols][1:])
Y = array(btc_up)
X_partial = array(merged[:][:300])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
Y_partial = array(btc_up[:300])


# Alternate model - 32-32-1, does not perform as well.
model = Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(1))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

model.fit(X_train, Y_train, epochs=5, batch_size=1)
ml5_mse, ml5_mae = model.evaluate(X_test, Y_test)

model.fit(X_train, Y_train, epochs=20, batch_size=1)
ml20_mse, ml20_mae = model.evaluate(X_test, Y_test)

comparison = [['persistence', persist_mae, persist_mse], ['ml5', ml5_mse, ml5_mae], ['ml20', ml20_mse, ml20_mae]]


seed = 7
numpy.random.seed(seed)

estimator = KerasClassifier(build_fn=baseline, nb_epoch=100, batch_size=5, verbose=0) kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print(results.mean()*100, results.std()*100)

# This predicts the price increase or decrease of btcOpen, in the form of a 1 or 0, respectively.

model = Sequential()
model.add(layers.Dense(64, activation='tanh', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(1))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

model.fit(X_train, Y_train, epochs=5, batch_size=1)
# model.fit(X, Y, epochs=5, batch_size=1)
ml5_mse, ml5_mae = model.evaluate(X_test, Y_test)

predictions = model.predict(X_test)
print(accuracy_score(Y_test, predictions))

        test_size = .33
seed = 7

model = SVC()
kfold = KFold(n_splits=6, random_state=7)
cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
print(cv_results.mean(), cv_results.std())

model.fit(X_train, Y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

print('Predictions for given dates:', predictions)
execfile('import.py')

models = []
models.append(('LR', LogisticRegression()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
results = []
names = []
scoring = 'accuracy'

# This runs model tests on all the coins. If mean accuracy is greater than .6, it prints the model and coin. 
for name, model in models:
    kfold = KFold(n_splits=10, random_state=7)
    for coin_predicted in y_df.columns:
        cv_results = cross_val_score(model, X, y_df[coin_predicted], cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "Accuracy of %s for %s: %f (+/- %0.2f)" % (name, coin_predicted, cv_results.mean(), cv_results.std() * 2)
        if cv_results.mean() > .6:
            print(msg)

# ------------------END MODEL TESTING -------------- #
