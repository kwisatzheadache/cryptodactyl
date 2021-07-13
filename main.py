import pickle
from dotenv import load_dotenv
import os
from coinbase.wallet.client import Client
import mariadb
from datetime import datetime
COINBASE_KEY=3ZtbY02UY4u6S5bXFBBVU+poy6ZLmm2Cw1yE701LZ0s9cKycvWRF7ShGFdEkfG01UdkOMDbqphR4uhqdeGaevg==
COINBASE_SECRET=402c5e248447641eec65ef14d955feb1

with open('coin_dictionary.p', 'rb') as f:
    converter_dictionary = pickle.load(f)

load_dotenv()
coinbase_key = os.environ.get('COINBASE_KEY')
coinbase_secret = os.environ.get('COINBASE_SECRET')
try:
    connection = mariadb.connect(user='cryptodactyl',
                                database='cryptodactyl',
                                password='asdqweW2',
                                host='cryptodactyl.cqisjzaosajb.us-west-1.rds.amazonaws.com',
                                port=3306)
    cursor = connection.cursor()
except Exception as e:
    print(e)
    print("DB connection isn't working. Are you remote or actually on the pi?")

if not coinbase_key:
    print("hey, there's no keey here")
else:
    print("well, guess that worked so far.")

    count = 0
    while count < 1:
        client = Client(coinbase_key, coinbase_secret)
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")

        rates = client.get_exchange_rates()
        exchange_rates = rates['rates']
        if not exchange_rates:
            print("shit's broken")
        else:
            coins = exchange_rates.keys()

            for coin in coins:
                try:
                    rate = 1/float(exchange_rates[coin])
                    print("price of {} is ${}".format(coin, rate))
                    cursor.execute('INSERT INTO entry (coin, value, time) VALUES (?, ?, ?)',
                                (coin, rate, time))
                    print("added to DB")
                except Exception as e:
                    print(e)

        try:
            connection.commit()
        except Exception as e:
            print(e)
        later = datetime.now()
        diff = later - now
        print("op time: {}".format(diff))
        print(len(rates['rates']))
        count += 1
