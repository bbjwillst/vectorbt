import sys
import os
import pandas as pd
import numpy as np
import vectorbt as vbt
from utils.FileExt import FileExt as fe


class Strategy:
    class SMA:
        def __init__(self, stockid: str=''):
            if not os.path.exists("datas/{}.csv".format(stockid)):
                print("file datas/{}.csv doesn't exist.".format(stockid))
                return

            f= fe()
            f.delete(filename=stockid, filetype='.txt', path='logs/')

            price_close = pd.read_csv("datas/{}.csv".format(stockid))[['close']]

            pairs = 30
            fast_ma_window = np.linspace(5, 35, pairs, dtype=int)
            slow_ma_window = np.linspace(15, 45, pairs, dtype=int)
            grid = np.array(np.meshgrid(fast_ma_window, slow_ma_window)).T.reshape(-1, 2)

            f = open("logs/{}.txt".format(stockid), 'a')

            for _ in grid:
                fast_ma = vbt.MA.run(price_close, _[0]) # fast line
                slow_ma = vbt.MA.run(price_close, _[1]) # slow line

                entries = fast_ma.ma_crossed_above(slow_ma)
                exits = fast_ma.ma_crossed_below(slow_ma)

                pf = vbt.Portfolio.from_signals(price_close, entries, exits, init_cash=100, fees=0.005)
                sys.stdout = f
                print(pf.total_return(), f)

            f.close()

    class OBV:
        def __init__(self, stockid: str=''):
            price_close = pd.read_csv("datas/{}.csv".format(stockid))[['close']]

            pairs = 30


