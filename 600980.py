import pandas as pd
import vectorbt as vbt
import vectorbt.indicators.factory
from utils.CollectEngine import CollectEngine as ce


if __name__ == "__main__":
    # Save stock data to csv
    # stocks = ce.Stocks()
    # stocks.getFullDataByTime("600980", start="2022-05-01", end="2022-11-15")

    price_close = pd.read_csv("datas/600980.csv")[["close"]]

    fast_ma: vectorbt.indicators.factory = vbt.MA.run(price_close, 10)
    slow_ma: vectorbt.indicators.factory = vbt.MA.run(price_close, 25)
    entries = fast_ma.ma_crossed_above(slow_ma)
    exists = fast_ma.ma_crossed_below(slow_ma)

    pf = vbt.Portfolio.from_signals(price_close, entries, exists, init_cash=1000)
    print(pf.stats())

