from pandas import read_csv
from pandas import merge
from pandas import DataFrame
from pandas import concat
import locale

btc = read_csv('./data/used/bitcoin_price.csv')
dash = read_csv('./data/used/dash_price.csv', header=0)
eth = read_csv('./data/used/ethereum_price.csv', header=0)
ethc = read_csv('./data/used/ethereum_classic_price.csv', header=0)
ltc = read_csv('./data/used/litecoin_price.csv', header=0)
monero = read_csv('./data/used/monero_price.csv', header=0)
ripple = read_csv('./data/used/ripple_price.csv', header=0)

coin_list = [btc, dash, eth, ethc, ltc, monero, ripple]
coin_names = ['btc', 'dash', 'eth', 'ethc', 'ltc', 'monero', 'ripple']

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

print('variable "merged" contains 409 days worth of market info for seven coins.')


# Some of the columns have a number with commas... remove them.
def no_comma(column):
    new = []
    for i in range(len(column)):
        new.append(column[i].replace(',', ''))
    return new


for column in merged.columns:
    if 'Volume' in column:
        merged[column] = no_comma(merged[column])
    if 'Market' in column:
        merged[column] = no_comma(merged[column])
    else:
        continue

print('Merged contains data for 7 coins')


# for i in merged.columns:
#     lagged = lag(merged[i], 7)
#     merged[lagged.columns] = lagged


print('Merged contains data for 7 coins')
