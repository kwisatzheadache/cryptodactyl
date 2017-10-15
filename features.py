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

