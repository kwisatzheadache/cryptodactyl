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

# Converting between coins
def convert(coin1, amount1, coin2, day):
    daily_prices = return_prices(day)
    ratio = daily_prices[coin1]/daily_prices[coin2]
    converted = amount1 * ratio
    return converted

def predict_ratios(day):

# ------------------- END FUNCTIONS -------------------#
