from matplotlib import pyplot
from keras.models import Sequential
from keras import models
from keras import layers
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
from scipy.stats.stats import pearsonr
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from statsmodels.tsa.seasonal import seasonal_decompose

btc_up = []

for i in range(len(input)):
    if input['btcClose'].iloc[i] < input['btcClose t - 1'].iloc[i]:
        btc_up.append(0)
    else:
        btc_up.append(1)

test_size = .2
seed = 7
Y = btc_up
X = input
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# Alternate model - 32-32-1, does not perform as well.
model = Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(1))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

model.fit(X_train, Y_train, epochs=5, batch_size=1)
ml5_mse, ml5_mae = model.evaluate(X_test, Y_test)

# model.fit(X_train, Y_train, epochs=20, batch_size=1)
# ml20_mse, ml20_mae = model.evaluate(X_test, Y_test)

# comparison = [['persistence', persist_mae, persist_mse], ['ml5', ml5_mse, ml5_mae], ['ml20', ml20_mse, ml20_mae]]

# print(comparison)
