import sys
import pandas as pd
import numpy as np
import vectorbt as vbt


if __name__ == "__main__":
    price_close = pd.read_csv("../../datas/600980.csv")[["close"]]

    num = 25
    fast_ma_window = np.linspace(5, 30, num, dtype=int)
    slow_ma_window = np.linspace(15, 40, num, dtype=int)
    grid = np.array(np.meshgrid(fast_ma_window, slow_ma_window)).T.reshape(-1, 2)

    f = open('1.txt', 'a')

    for _ in grid:
        fast_ma = vbt.MA.run(price_close, _[0])
        slow_ma = vbt.MA.run(price_close, _[1])

        entries = fast_ma.ma_crossed_above(slow_ma)
        exits = fast_ma.ma_crossed_below(slow_ma)

        pf = vbt.Portfolio.from_signals(price_close, entries, exits, init_cash=100, fees=0.005)
        sys.stdout = f
        print(pf.total_return(), f)
        print('========================================================')

    f.close()


    #
    # for _ in grid:
    #     fast_ma = vbt.MA.run(price_close, _[0])  # _[0]
    #     slow_ma = vbt.MA.run(price_close, _[1])  # _[1]
    #
    #     entries = fast_ma.ma_crossed_above(slow_ma)
    #     exits = fast_ma.ma_crossed_below(slow_ma)
    #
    #     pf = vbt.Portfolio.from_signals(price_close, entries, exits, init_cash=100, fees=0.005)
    #
    #     with open('1.txt', 'a') as f:
    #         sys.stdout = f
    #         print(pf.total_return(), f)
    #         print("========================================")



