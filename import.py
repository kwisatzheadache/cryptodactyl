from pandas import read_csv
from pandas import merge
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
def remove_commas(column):
    newcolumn = []
    for i in range(len(column)):
        newcolumn.append(locale.atoi(column[i]))
    return newcolumn

# def remove_commas(column):
#     for i in range(len(column)):
#         column[i] = locale.atoi(column[i])

for column in merged.columns:
    if 'Volume' in column:
        merged[column] = remove_commas(merged[column])
    if 'Market' in column:
        merged[column] = remove_commas(merged[column])
    else:
        print('this column works')

print(merged.head(3))
