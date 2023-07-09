import sys
import os
import pandas as pd
import numpy as np
import vectorbt as vbt
from vectorbt.portfolio.base import PortfolioT

from stocks.datas import stock_dict
from utils.FileExt import FileExt as fe
from utils.GlobalPaths import g_data_path, g_log_path


class Strategy:
    class MA:
        def __init__(self, stockid: str = ''):
            if not os.path.exists(g_data_path + "{}.csv".format(stockid)):
                print("file datas/{}.csv doesn't exist.".format(stockid))
                return

            f = fe()
            f.delete(filename=stockid, filetype='.txt', path='logs/')

            price_close = pd.read_csv("datas/{}.csv".format(stockid))[['close']]

            windows = np.arange(5, 60)
            fast_ma, slow_ma = vbt.MA.run_combs(price_close, window=windows, r=2, short_names=['fast', 'slow'])
            entries = fast_ma.ma_crossed_above(slow_ma)
            exits = fast_ma.ma_crossed_below(slow_ma)

            pf: vbt.Portfolio = vbt.Portfolio.from_signals(price_close, entries, exits, fees=0.005, freq='1D')
            pf.total_return().vbt.heatmap(
                x_level='fast_window', y_level='slow_window', symmetric=True,
                trace_kwargs=dict(colorbar=dict(title='Total return', tickformat='%'))
            ).show()

    class SMA:
        def __init__(self, stockid: str = ''):
            if stockid not in stock_dict:
                print(f"【{stockid}】 is not in the datas.py file!")
                return

            if not os.path.exists(g_data_path + "{}.csv".format(stockid)):
                print("file datas/{}.csv doesn't exist.".format(stockid))
                return

            f = fe()
            f.delete(filename=stockid, filetype='.txt', path=g_log_path)

            price_close = pd.read_csv(g_data_path + "{}.csv".format(stockid))[['close']]

            pairs = 40
            fast_ma_window = np.linspace(5, 5 + pairs, pairs, dtype=int)
            slow_ma_window = np.linspace(10, 10 + pairs, pairs, dtype=int)
            grid = np.array(np.meshgrid(fast_ma_window, slow_ma_window)).T.reshape(-1, 2)

            f = open(g_log_path + "{}.txt".format(stockid), 'a')

            for _ in grid:
                fast_ma = vbt.MA.run(price_close, _[0])  # fast line
                slow_ma = vbt.MA.run(price_close, _[1])  # slow line

                entries = fast_ma.ma_crossed_above(slow_ma)
                exits = fast_ma.ma_crossed_below(slow_ma)

                pf: PortfolioT = vbt.Portfolio.from_signals(price_close, entries, exits, init_cash=100, fees=0.0015)
                sys.stdout = f
                print(pf.total_return(), f)

            f.close()

    class OBV:
        def __init__(self, stockid: str = ''):
            if stockid not in stock_dict:
                print(f"【{stockid}】 is not in the datas.py file!")
                return

            if not os.path.exists(g_data_path + "{}.csv".format(stockid)):
                print("file datas/{}.csv doesn't exist.".format(stockid))
                return

            f = fe()
            f.delete(filename=stockid, filetype='.txt', path=g_log_path)

            price_close = pd.read_csv(g_data_path + "{}.csv".format(stockid))[['close']]
            volume_close = pd.read_csv(g_data_path + "{}.csv".format(stockid))[['volume']]

            obv_start = 3
            obv_end = 300
            obv_window = np.linspace(obv_start, obv_end, obv_end - obv_start, dtype=int)

            for _ in obv_window:
                vbt.OBV.run(price_close, volume_close)



    class RSI:
        def __init__(self, stockid: str = ''):
            if stockid not in stock_dict:
                print(f"【{stockid}】 is not in the datas.py file!")
                return

            if not os.path.exists(g_data_path + "{}.csv".format(stockid)):
                print("file datas/{}.csv doesn't exist.".format(stockid))
                return

            f = fe()
            f.delete(filename=stockid, filetype='.txt', path=g_log_path)

            price_close = pd.read_csv(g_data_path + "{}.csv".format(stockid))[['close']]

            