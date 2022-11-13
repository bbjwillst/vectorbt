import pandas as pd
import tushare as ts


class CollectEngine:
    class Stocks:
        def __init__(self):
            pass

        def getFullData(self, stock_id=""):
            df: pd.DataFrame = ts.get_hist_data(stock_id)
            df.to_csv("datas/{}.csv".format(stock_id))

        def getFullDataByTime(self, stock_id="", start="", end=""):
            df: pd.DataFrame = ts.get_hist_data(stock_id, start=start, end=end)
            df.to_csv("datas/{}.csv".format(stock_id))
