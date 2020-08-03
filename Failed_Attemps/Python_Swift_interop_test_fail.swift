import PythonKit

let pandas = Python.import("pandas")
let numpy = Python.import("numpy")
let tradeapi = Python.import("alpaca_trade_api")

let base_url: PythonObject = "https://api.alpaca.markets"
let key_id: PythonObject = ""
let secret_key: PythonObject = ""

let api: PythonObject = tradeapi.REST(base_url, key_id, secret_key)

let multiplier: PythonObject = 1
let timespan: PythonObject = "minute"
let _from: PythonObject = "2019-04-01"
let to: PythonObject = "2019-04-02"

let aapl: PythonObject = api.polygon.historic_agg_v2("AAPL", multiplier, timespan, _from, to).df // Everything works up until here.
