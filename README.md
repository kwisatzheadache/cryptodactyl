## Synopsis

Development of neural nets to predict market volatility in cryptocurrencies.

## Code Example

`python master.py` imports data from 7 cryptocurrencies and uses Support Vector Classification to  fit an NN model to the data. The model can the be used to predict whether the price of bitcoin for a given tomorrow will be higher or lower than the given today.


## Motivation

Why do we do anything in life?

## Notes

Current dataset is in reverse chronological order. Thinking about reversing it so that day one is in the past, rather than the most recent day...

## Next Steps

Automate collection of coin data.
Analyze other coins.
Address seasonality and general trend of data.
Increase frequency of sampling to hourly. 

## Tests


## License

MIT
