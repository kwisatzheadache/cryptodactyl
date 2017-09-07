from pandas import Series
from pandas import read_csv
from pandas import concat
from matplotlib import pyplot
from pandas import DataFrame
import pandas as pd
# import keras
# import tensorflow


btc = read_csv('./bitcoin_price.csv')
dash = read_csv('./dash_price.csv', header=0)
eth = read_csv('ethereum_price.csv', header=0)
ethc = read_csv('ethereum_classic_price.csv', header=0)
ltc = read_csv('litecoin_price.csv', header=0)
monero = read_csv('monero_price.csv', header=0)
ripple = read_csv('ripple_price.csv', header=0)

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
merged = reduce(lambda left,right: pd.merge(left,right,on='Date'), coin_list)



