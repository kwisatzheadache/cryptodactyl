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

# At the end of the trading cycle (100 days), figure the change in value without trades.
# $250 in each coin from start date to finish.
# Base all starting values on open or close... arbitrarily lets pick close.

BTC = 250
ETH = 250
LTC = 250
MON = 250

# Ratio analysis will look like this: BTC_LTC = 1
# Ratios will be an array?
# [['BTC_LTC', 1]
#  ['BTC_ETH', 0]
#   ............
#  ['LTC_MON', 1]]

def ratio_analysis():


holdings = [BTC, ETH, LTC, MON]
def trade(ratios, monies):
