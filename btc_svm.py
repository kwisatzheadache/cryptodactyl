from sklearn.svm import SVC
model = SVC()
kfold = KFold(n_splits=6, random_state=7)
cv_results = cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
print(cv_results.mean(), cv_results.std())


for i in date:
    cols = []
    for j in range(8):
        cols.append(i+str(j))
    df[cols] = lag(merged[i], 7)
