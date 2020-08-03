import PythonKit

let os = Python.import("os")
let sys = Python.import("sys")
sys.path.append(os.getcwd())

let alpaca = Python.import("histo_trades_1min_alpaca")
let dict: PythonObject = [alpaca.get_ticker_history()] // Will get $AAPL as default
print(dict)
