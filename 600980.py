import pandas as pd
import numpy as np
import vectorbt as vbt
import vectorbt.indicators.factory
from utils.CollectEngine import CollectEngine as ce


if __name__ == "__main__":
    # Save stock data to csv
    # stocks = ce.Stocks()
    # stocks.getFullDataByTime("600980", start="2021-11-16", end="2022-11-16")

    price_close = pd.read_csv("datas/600980.csv")[["close"]]

    num = 10
    fast_ma_window = np.linspace(10, 20, num, dtype=int)
    slow_ma_window = np.linspace(20, 30, num, dtype=int)
    grid = np.array(np.meshgrid(fast_ma_window, slow_ma_window)).T.reshape(-1, 2)

    for _ in grid:
        fast_ma = vbt.MA.run(price_close, _[0])
        slow_ma = vbt.MA.run(price_close, _[1])

        entries = fast_ma.ma_crossed_above(slow_ma)
        exits = fast_ma.ma_crossed_below(slow_ma)

        pf = vbt.Portfolio.from_signals(price_close, entries, exits, init_cash=100, fees=0.0005)
        print(pf.total_return())
        print("========================================")



