import vectorbt as vbt
import numpy as np
import pandas as pd
import vectorbt.indicators.factory
import yfinance as yf


btc_price = pd.read_csv("datas/BTCUSD.csv")[["Date", "Open", "High", "Low", "Close", "Volume"]]
btc_price = btc_price.set_index("Date")

price = btc_price.get("Close")

fast_ma: vectorbt.indicators.factory = vbt.MA.run(price, 20)
slow_ma: vectorbt.indicators.factory = vbt.MA.run(price, 60)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100)
print(pf.total_profit())


# entries = rsi.rsi_crossed_below(20)
# exits = rsi.rsi_crossed_above(80)
#
# pf = vbt.Portfolio.from_signals(btc_price, entries, exits, init_cash=100)
# print(pf.stats())