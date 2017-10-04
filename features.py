# Feature Engineering

# Creating variable to track ratios: btc:ltc, ltc:eth, btc:eth, etc. Questions - do I take an average of the ratio? A rolling average? Try to predict change in average, or just increase/decrease in ratio.

# Predictor of which coin has greatest rise/fall.
from matplotlib import pyplot

# coin ratios

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


# pyplot.plot(btc_ltc)
# pyplot.plot(btc_eth)
# pyplot.plot(btc_mon)
# pyplot.plot(ltc_eth)
# pyplot.plot(ltc_mon)
# pyplot.plot(eth_mon)
# pyplot.show()
