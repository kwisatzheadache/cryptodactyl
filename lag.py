def lag(variable, window):
    df1 = DataFrame(variable)
    for i in range(window):
        j = window - i
        df1 = concat([df1, variable.shift(j)], axis=1)
    columns = [variable.name]
    for i in range(window):
        j = window - i
        columns.append('t - %d' % j)
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

