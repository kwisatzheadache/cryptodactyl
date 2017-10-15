from keras import layers
from keras import models
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasClassifier
from math import sqrt
from matplotlib import pyplot
from numpy  import array
from numpy import array
from pandas import DataFrame
from pandas import concat
from pandas import merge
from pandas import read_csv
from pandas.tools.plotting import autocorrelation_plot
from pandas.tools.plotting import lag_plot
from scipy.stats.stats import pearsonr
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy
import pandas

# ----------------- BEGIN FUNCTIONS ---------------# 
# Creates a df with columns [T, t-1, t-2, ... t-window]
def lag(variable, window):
    df1 = DataFrame(variable)
    for i in range(window):
        j = window - i
        df1 = concat([df1, variable.shift(j)], axis=1)
    columns = [variable.name]
    for i in range(window):
        j = window - i
        columns.append(variable.name + ' t - %d' % j)
    df1.columns = columns
    return df1.iloc[window:]

# Simplest prediction model. Predicts T will be equal to T-1
def persist(x):
    xy = lag(x, 1)
    col = xy.columns
    y_hat = xy[xy.columns[0]]
    y = xy[xy.columns[1]]
    error = []
    for i in range(len(xy)):
        delta = (y_hat[i+1] - y[i+1])
        error.append(delta)
    mae = sum(abs(err) for err in error)/len(error)
    mse = sum(err*err for err in error)/len(error)
    return (mae, mse)

# Remove commas
def no_comma(column):
    new = []
    for i in range(len(column)):
        new.append(column[i].replace(',', ''))
    return new

# Finds the prices of coins at close given the day.
def return_prices(day):
    btc = merged.loc[day, 'btcClose']
    ltc = merged.loc[day, 'ltcClose']
    eth = merged.loc[day, 'ethClose']
    mon = merged.loc[day, 'moneroClose']
    return {
        'btc': btc, 'ltc': ltc, 'eth': eth, 'mon': mon
    }

# Takes the given dataset and column. Outputs whether value at T is greater or lesser than value at T-1
def make_y(dataset, coin):
    coin_up = []
    lookback = lag(dataset[coin], 1)
    cols = lookback.columns
    for i in range(len(lookback)):
        if lookback[cols[0]].iloc[i] < lookback[cols[1]].iloc[i]:
            coin_up.append(0)
        else:
            coin_up.append(1)
    return coin_up

# Receive purchase call and return coin amount
def purchase(coin, dollars, day):
    daily_prices = return_prices(day)
    amount = dollars * (1 / daily_prices[coin])
    return amount

# ------------------- END FUNCTIONS -------------------#

# -------- BEGIN IMPORTING AND ARRANGING DATA ---------#
btc = read_csv('./data/used/bitcoin_price.csv')
dash = read_csv('./data/used/dash_price.csv', header=0)
eth = read_csv('./data/used/ethereum_price.csv', header=0)
ethc = read_csv('./data/used/ethereum_classic_price.csv', header=0)
ltc = read_csv('./data/used/litecoin_price.csv', header=0)
monero = read_csv('./data/used/monero_price.csv', header=0)
ripple = read_csv('./data/used/ripple_price.csv', header=0)

coin_list = [btc, dash, eth, ethc, ltc, monero, ripple]
coin_names = ['btc', 'dash', 'eth', 'ethc', 'ltc', 'monero', 'ripple']
# Add coin name to beginning of columns, so that when coin data is merged, information remains easily identified by coin.
for coin in range(len(coin_list)):
    columns = []
    name = coin_names[coin]
    for j in coin_list[coin].columns:
        if j == 'Date':
            columns.append(j)
        else:
            columns.append(name+j)
    coin_list[coin].columns = columns

# Trim input to smallest list
size = []
for coin in coin_list:
    size.append(len(coin))

for i in range(len(coin_list)):
    coin_list[i] = coin_list[i][0:min(size)]

# Combine coins into one large df
merged = reduce(lambda left,right: merge(left,right,on='Date'), coin_list)
merged['counter'] = range(len(merged))
cols = list(merged.columns)
cols.insert(0, cols.pop(cols.index('counter')))
merged = merged[cols]

# Some of the columns have a number with commas... remove them.
for column in merged.columns:
    if 'Volume' in column:
        merged[column] = no_comma(merged[column])
    if 'Market' in column:
        merged[column] = no_comma(merged[column])
    else:
        continue

# -------- END IMPORTING AND ARRANGING DATA ---------#


# ------------- BEGIN CREATING FEATURES -------------#


with_ratios = DataFrame(merged)
ratios = [('btc_ltc', btc_ltc), ('btc_eth', btc_eth), ('btc_mon', btc_mon), ('ltc_eth', ltc_eth), ('ltc_mon', ltc_mon), ('eth_mon', eth_mon)]
for name, data in ratios:
    with_ratios[name] = data
# with_ratios['btc_ltc', 'btc_eth', 'btc_mon', 'ltc_eth', 'ltc_mon', 'eth_mon'] = [btc_ltc, btc_eth, btc_mon, ltc_eth, ltc_mon, eth_mon]

cols = array(merged.columns)[1:]
X = array(merged[cols][1:])
#Y is selected from the columns of y_df - a df with derived in y_coins.py

# ------------- END CREATING FEATURES ---------------#


# ------------- BEGIN MAKING Y-SET ------------------#

# Creating variable to track ratios: btc:ltc, ltc:eth, btc:eth, etc. Questions - do I take an average of the ratio? A rolling average? Try to predict change in average, or just increase/decrease in ratio.
# coin ratios

btc_up = []
lookback = lag(merged['btcClose'], 1)

for i in range(len(lookback)):
    if lookback['btcClose'].iloc[i] < lookback['btcClose t - 1'].iloc[i]:
        btc_up.append(0)
    else:
        btc_up.append(1)


############

# Not entirely sure how I was going to use this. "If today's value is less than yesterday's y_list[i] = 0, else 1." That's the idea of it. 
y_list = []
for i in merged.columns:
    if 'High' in i:
        y_list.append(i)
    if 'Open' in i:
        y_list.append(i)
    if 'Close' in i:
        y_list.append(i)
    if 'Low' in i:
        y_list.append(i)
    else:
        continue

y_df = DataFrame()
for i in y_list:
    y_df[i] = make_y(merged, i)

############

btc_ltc = []
for i in range(len(merged)):
    btc_ltc.append(merged['btcClose'][i]/merged['ltcClose'][i])

btc_eth = []
for i in range(len(merged)):
    btc_eth.append(merged['btcClose'][i]/merged['ethClose'][i])

btc_mon = []
for i in range(len(merged)):
    btc_mon.append(merged['btcClose'][i]/merged['moneroClose'][i])

ltc_eth = []
for i in range(len(merged)):
    ltc_eth.append(merged['ltcClose'][i]/merged['ethClose'][i])

ltc_mon = []
for i in range(len(merged)):
    ltc_mon.append(merged['ltcClose'][i]/merged['moneroClose'][i])

eth_mon = []
for i in range(len(merged)):
    eth_mon.append(merged['ethClose'][i]/merged['moneroClose'][i])

# ------------- END MAKING Y-SET ------------------- #

# ----------------BEGIN MODEL TESTING -------------- #


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

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

cols = array(merged.columns)[1:]
Y_partial = array(btc_up[:300])
X_partial = array(merged[:][:300])

Y = array(btc_up)
X = array(merged[cols][1:])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

estimator = KerasClassifier(build_fn=baseline, nb_epoch=100, batch_size=5, verbose=0) kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print(results.mean()*100, results.std()*100)

# This predicts the price increase or decrease of btcOpen, in the form of a 1 or 0, respectively.

        test_size = .33
seed = 7
cols = array(merged.columns)[1:]
Y_partial = array(btc_up[:300])
X_partial = array(merged[:][:300])

Y = array(btc_up)
X = array(merged[cols][1:])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


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
execfile('import.py')
# ------------------END MODEL TESTING -------------- #


# --------------------- BEGIN TRADING -------------- #

# Start with $1000 in four coins = monero, bitcoin, litecoin, and ethereum.
# Based on the prediction of the ratio analyses, trade between the four coins.
# Run on a daily basis.
# For each ratio higher, trade 25% of holdings to that coin.

# Example $250 Eth, $250 LTC, $250 BTC, $250 MON
# BTC_LTC up: receive 25% of LTC as BTC -> $312.5 BTC, $187.5 LTC
# BTC_ETH down: trade 25% of BTC for ETH
# BTC_MON down: trade 25% of BTC for MON
# ETH_LTC up: receive 25% of LTC as ETH
# ETH_MON down: trade 25% of ETH as MON
# LTC_MON down: trade 25% of LTC as MON


# However, coins must be purchased, not just held as dollars......
# At purchase, grab the price of each coin at close, then convert dollars to coins.
# Daily, grab coin prices so that holdings can be converted at current rates.

# At the end of the trading cycle (100 days), figure the change in value without trades.
# $250 in each coin from start date to finish.
# Base all starting values on open or close... arbitrarily lets pick close.

BTC = purchase('btc', 250, 1)
ETH = purchase('eth', 250, 1)
LTC = purchase('ltc', 250, 1)
MON = purchase('mon', 250, 1)

# Converting between coins
def convert(coin1, amount1, coin2, day):
    daily_prices = return_prices(day)
    ratio = daily_prices[coin1]/daily_prices[coin2]
    converted = amount1 * ratio
    return converted

def predict_ratios(day):

# Ratio analysis will look like this: BTC_LTC = 1
# Ratios will be an array?
# [['BTC_LTC', 1]
#  ['BTC_ETH', 0]
#   ............
#  ['LTC_MON', 1]]

# def ratio_analysis():


# holdings = [BTC, ETH, LTC, MON]
# def trade(ratios, monies):

# ----------------- END TRADING ------------------ #


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

execfile('import.py')


print 'y_df contains predicted increases for coins'
