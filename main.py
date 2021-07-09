from dotenv import load_dotenv
import os
from coinbase.wallet.client import Client

load_dotenv()
coinbase_key = os.environ.get('COINBASE_KEY')
coinbase_secret = os.environ.get('COINBASE_SECRET')

if not coinbase_key:
    print("hey, there's no keey here")
else:
    print("well, guess that worked so far.")

    client = Client(coinbase_key, coinbase_secret)

    rates = client.get_exchange_rates()
    exchange_rates = rates['rates']
    if not exchange_rates:
        print("shit's broken")
    else:
        coins = exchange_rates.keys()

        for coin in coins:
            rate = 1/float(exchange_rates[coin])
            print("price of {} is ${}".format(coin, rate))

    btc = exchange_rates['BTC']
    if btc:
        btc = 1/float(btc)
        print("BTC is ${}".format(btc))
    else:
        print("BTC not in this data, for some reason.")


