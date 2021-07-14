import pickle
import os
import mariadb
import time
from coinbase.wallet.client import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
COINBASE_KEY = os.environ.get('COINBASE_KEY')
COINBASE_SECRET = os.environ.get('COINBASE_SECRET')
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


count = 0
while count < 600:
    if count % 10 == 0:
        # Not sure if connection or cursor is going to cause issues, so I'll just reload it every 10 seconds.
        try:
            connection = mariadb.connect(user='cryptodactyl',
                                        database='cryptodactyl',
                                        password='asdqweW2',
                                        host='cryptodactyl.cqisjzaosajb.us-west-1.rds.amazonaws.com',
                                        port=3306)
            cursor = connection.cursor()
            client = Client(COINBASE_KEY, COINBASE_SECRET)
        except Exception as e:
            print(e)
            print("DB connection isn't working. Are you remote or actually on the pi?")

    data = []
    now = datetime.now()
    curr_time = now.strftime("%Y-%m-%d %H:%M:%S")

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
                data.append([coin, rate, curr_time])
                print("added to DB")
            except Exception as e:
                print(e)

    try:
        cursor.executemany(QUERY, data)
        connection.commit()
    except Exception as e:
        print(e)
    later = datetime.now()
    diff = later - now
    print("op time: {}".format(diff))
    print(len(rates['rates']))
    microdiff = diff.microseconds/1000000
    if microdiff >= 1:
        microdiff = 0
    time.sleep(1-microdiff)
    count += 1
