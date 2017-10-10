execfile('import.py')

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

def return_prices(day):
    btc = merged.loc[day, 'btcClose']
    ltc = merged.loc[day, 'ltcClose']
    eth = merged.loc[day, 'ethClose']
    mon = merged.loc[day, 'moneroClose']
    return {
        'btc': btc, 'ltc': ltc, 'eth': eth, 'mon': mon
    }

# Receive purchase call and return coin amount
def purchase(coin, dollars, day):
    daily_prices = return_prices(day)
    amount = dollars * (1 / daily_prices[coin])
    return amount

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


