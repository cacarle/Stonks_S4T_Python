import pandas
import numpy as np
import alpaca_trade_api as tradeapi

ticker_default = "AAPL"

def get_ticker_history(ticker=ticker_default):
    base_url = 'https://api.alpaca.markets'
    api_key_id = '' # Input your Key ID
    api_secret = '' # Input your Secret Key

    api = tradeapi.REST(base_url=base_url, key_id=api_key_id,
                        secret_key=api_secret)

    ticker_df = api.polygon.historic_agg_v2(ticker, multiplier=1, timespan='minute',
                                        _from='2019-04-01', to='2019-04-10').df

    # We are converting to numpy because there is no official support for pandas
    ticker_vals_np = ticker_df.to_numpy()
    # After conversion the keys (timestamps) are lost so we can make a new array
    ticker_idx_np = ticker_df.index.to_numpy()

    # Initialize the dictionary to contain everything
    stock_dict = {}

    for i in range(len(ticker_idx_np)):
        stock_dict[ticker_idx_np[i]] = ticker_vals_np[i]

    # dict(itertools.islice(stock_dict.items(), n)) To output the first n
    # key/value pairs for testing. Don't forget to import itertools for this
    return stock_dict
