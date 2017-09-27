## Synopsis

Development of neural nets to predict market volatility in cryptocurrencies.

## Code Example

`python btc_svm` imports data from 7 cryptocurrencies and uses Support Vector Classification to  fit an NN model to the data. The model then predicts whether the price of bitcoin for a given tomorrow will be higher or lower than the given today.


## Motivation

Why do we do anything in life?

## Next Steps

Normalize Data to provide nn with less variability.
Automate collection of coin data.
Analyze other coins.
Address seasonality and general trend of data.
Increase frequency of sampling to hourly. 

## Tests

`model_testing.py` runs a series of coin indices through various models and outputs information for any model which predicts accuracy greater than 60%.
However, most of these have a rather unacceptable confidence intervale, though I will work to improve this by increasing sampling rates.

## Contributors

mndvns and kwisatzheadache

## License

MIT
