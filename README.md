## Synopsis
High frequency trading. But not the way that FinTech companies are doing - thousands of trades per hour, dependent on high-speed connection and execution. Rather, we're trading on lower-frequency volatility, in smaller dollar amounts.

Currently unclear whether it will be strictly stocks, coins, or a mix of both. 

Multiple parts:

1. API to scrape and collate data. Store in database. Thinking Elixir/MySQL, running on raspberry pi.
1. Analysis and simulation. Things to consider:
11. First layer: modeling single good.
11. Second layer: multiple goods.
11. Third layer: mixing trading strategies.
11. Sampling frequency.
11. Return requirements and stop losses.


## Code Example
None yet.



## Motivation
$$$$$$$$$$$$$$$$


## Notes


## Next Steps
`sudo apt install mariadb-server-10.3`
1. mariaDB server
Create database "cryptodactyl"
create table "ticker" with columns: `id, name, value, timestamp, source`
1. simple API calls with python `requests`
11. Grab multiple tickets, store in db.
11. Run on Raspberry pi
1. Modeling and simulation. Probably in Python for ease and speed.


## Requirements
1. python requirements in requirements.txt. Install with `pip3 install -r requirements.txt`
1. mariadb. Install for raspbian not done yet.



## Tests
None yet.


## License

MIT
