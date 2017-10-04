# Feature Engineering

# Creating variable to track ratios: btc:ltc, ltc:eth, btc:eth, etc. Questions - do I take an average of the ratio? A rolling average? Try to predict change in average, or just increase/decrease in ratio.

# Predictor of which coin has greatest rise/fall.
from matplotlib import pyplot

execfile('import.py')

# btc:ltc ratio

btc_ltc = []
for i in range(len(merged)):
    btc_ltc.append(merged['btcClose'][i]/merged['ltcClose'][i])

btc_eth = []
for i in range(len(merged)):
    btc_eth.append(merged['btcClose'][i]/merged['ethClose'][i])

eth_ltc = []
for i in range(len(merged)):
    eth_ltc.append(merged['ethClose'][i]/merged['ltcClose'][i])


pyplot.plot(btc_ltc)
pyplot.plot(eth_ltc)
pyplot.plot(btc_eth)
pyplot.show()
