
import pickle
import os
import mariadb
import time
from coinbase.wallet.client import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
COINBASE_KEY="3ZtbY02UY4u6S5bXFBBVU+poy6ZLmm2Cw1yE701LZ0s9cKycvWRF7ShGFdEkfG01UdkOMDbqphR4uhqdeGaevg=="
COINBASE_SECRET="402c5e248447641eec65ef14d955feb1"
# COINBASE_KEY = os.environ.get('COINBASE_KEY')
# COINBASE_SECRET = os.environ.get('COINBASE_SECRET')
QUERY = 'INSERT INTO entry (coin, value, time) VALUES (?, ?, ?)'

try:
    connection = mariadb.connect(user='cryptodactyl',
                                database='cryptodactyl',
                                password='cryptodactyl',
                                host='cryptodactyl.cqisjzaosajb.us-west-1.rds.amazonaws.com',
                                port=3306)
    cursor = connection.cursor()
    client = Client(COINBASE_KEY, COINBASE_SECRET)
except Exception as e:
    print(e)
    print("DB connection isn't working. Are you remote or actually on the pi?")

def get_coin(coin_id='BTC'):
    # This query is taking a long time. For now, let's just run it once and use that vector while we start writing the analysis stuff.
    # query = "SELECT coin, value, time FROM entry WHERE coin LIKE '{}' and time between '2021-08-01' and '2021-08-02';".format(coin_id)
    # cursor.execute(query)
    # return cursor
    with open('btc-2021-08-02.p', 'rb') as f:
        data = pickle.load(f)

    return data
