from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

lagged = DataFrame()
for i in merged.columns:
    column = merged[i]
    lagged = lagged.append(lag(column, 7))

