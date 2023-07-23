import os
import pandas as pd
import numpy as np
import vectorbt as vbt
from vectorbt.portfolio.base import PortfolioT

from stocks.datas import stock_dict
from utils.FileExt import FileExt as fe
from utils.GlobalPaths import g_data_path, g_log_path


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
        obv_end = 100
        obv_window = np.linspace(obv_start, obv_end, obv_end - obv_start, dtype=int)

        for _ in obv_window:
            vbt.OBV.run(price_close, volume_close)

