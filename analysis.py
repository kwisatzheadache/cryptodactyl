from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

for i in merged.columns:
    lagged = lag(merged[i], 7)
    merged[lagged.columns] = lagged
