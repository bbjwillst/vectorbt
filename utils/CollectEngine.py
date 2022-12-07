import pandas as pd
import tushare as ts
from utils.FileExt import FileExt as fe


class CollectEngine:
    class Stocks:
        @staticmethod
        def getfulldata(stock_id=""):
            f = fe()
            f.delete(stock_id)
            df: pd.DataFrame = ts.get_hist_data(stock_id)
            df.to_csv("datas/{}.csv".format(stock_id))

        @staticmethod
        def getfulldatabytime(stock_id="", start="", end=""):
            f = fe()
            f.delete(stock_id)
            df: pd.DataFrame = ts.get_hist_data(stock_id, start=start, end=end)
            df.to_csv("datas/{}.csv".format(stock_id))
