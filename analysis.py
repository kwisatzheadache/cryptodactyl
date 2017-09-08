from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
filename = './data/used/bitcoin_price.csv'
dataframe = read_csv(filename)

