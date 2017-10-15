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
