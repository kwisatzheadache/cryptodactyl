from sklearn.svm import SVC


execfile('import.py')

model = SVC()
kfold = KFold(n_splits=6, random_state=7)
cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
print(cv_results.mean(), cv_results.std())


predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

print('Predictions made with accuracy of %d' % accuracy)
