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


print 'y_df contains predicted increases for coins'
