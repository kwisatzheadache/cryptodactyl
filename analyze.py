import math
# Hello, Michael.

# Outline the steps:
"""
1. Import data and vectorize
2. Select trading method
3. For each window, make trade decision.
4. Determine success of trade algo

"""

BUY = 1
SELL = -1
HOLD = 0
HAVE_COINS = 1
HAVE_NO_COINS = 0

def get_data(coin_id):
    data_vector = []
    return data_vector

# holding_state: 0 = we have no coins
#                1 = we have coins
# holding_state = 0
# coin = "BTC"
# data_vector = get_data(coin)
# window_size = 10
# for window in range(len(data_vector)-window_size):
#     snippet = data_vector[window:window+window_size]
#     trade_decision = make_decision(snippet, method="Default")
#     if trade_decision


def make_decision(snippet, method="Default"):
    """
    For a given window of coin values, we want to decide whether to buy, sell, or do nothing.
    """
    decision_method = {"Default": repeating_direction,
                       "Repeating Direction": repeating_direction,
                       "Regression to Mean": repeating_direction,
                       0: repeating_direction,
                       None: repeating_direction}
    decision = decision_method[method](snippet)
    return decision

def repeating_direction(snippet):
    """
    Using regression to the mean idea. Count direction of change between each step. If more negative changes, anticipate positive change. If more positive, anticipate negative.
    If we anticipate positive change, we think the price is going to rise, so we buy.
    """
    positive_change = 0
    negative_change = 0
    for step in range(len(snippet)-1):
        delta = snippet[step+1] - snippet[step]
        if delta > 0:
            positive_change += 1
        elif delta < 0:
            negative_change += 1
        else:
            pass
    threshold = len(snippet) * 2/3
    # Anticipated change is opposite of current change count
    print("Threshold: {}".format(threshold))
    print("positive_change: {}".format(positive_change))
    print("negative_change: {}".format(negative_change))
    if positive_change > threshold:
        return SELL
    elif negative_change > threshold:
        return BUY
    else:
        return HOLD

def trade_over_entire_series(price_vector, starting_amount=1, window_size=10, sampling_rate=1, coin_id="BTC", decision_method="Default"):
    """
    Start with <starting_amount>, at every window, make a decision to buy, sell, or hold.
    """
    current_cash_value = starting_amount * price_vector[window_size]
    starting_cash_value = starting_amount * price_vector[0]
    ending_cash_value = starting_amount * price_vector[-1]

    holding_state = HAVE_NO_COINS
    holding_amount = 0
    total_windows = math.floor(len(price_vector)/window_size)
    for window in range(total_windows):
        start = window * window_size
        end = (window + 1) * (window_size-1)
        snippet = price_vector[start:end]
        current_price = price_vector[end]
        decision = make_decision(snippet)
        # Have no holdings, only cash, so we're looking to buy
        if decision == BUY and holding_state == HAVE_NO_COINS:
            # We "buy"
            holding_amount = current_cash_value / current_price
        elif decision == SELL and holding_state == HAVE_COINS:
            current_cash_value = holding_amount * current_price
        else:
            pass
    return (starting_cash_value, ending_cash_value, current_cash_value)


def convert_queryresult_to_price_vector(query_result):
    """
    MariaDB query returns a list of tuples:
    [(coin_id, value, time),
     (coin_id, value, time),
     ...
    ]
    This fetches the value column.
    """
    zipped = zip(query_result)
    return zipped(1)
