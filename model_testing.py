from sklearn.model_selection import train_test_split
from numpy import array
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

execfile('import.py')
execfile('y_coins.py')

with_ratios = merged
ratios = [('btc_ltc', btc_ltc), ('btc_eth', btc_eth), ('btc_mon', btc_mon), ('ltc_eth', ltc_eth), ('ltc_mon', ltc_mon), ('eth_mon', eth_mon)]
for name, data in ratios:
    with_ratios[name] = data
# with_ratios['btc_ltc', 'btc_eth', 'btc_mon', 'ltc_eth', 'ltc_mon', 'eth_mon'] = [btc_ltc, btc_eth, btc_mon, ltc_eth, ltc_mon, eth_mon]

cols = array(merged.columns)[1:]
X = array(merged[cols][1:])
#Y is selected from the columns of y_df - a df with derived in y_coins.py

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


# Strangely enough, the merged df contains columns from with_ratios. Not sure why or how that works, will have to look into it.

