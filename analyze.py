
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
