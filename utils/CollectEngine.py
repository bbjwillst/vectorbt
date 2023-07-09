import datetime
import pandas as pd
import tushare as ts

from stocks.datas import stock_dict
from utils.FileExt import FileExt as fe
from utils.GlobalPaths import g_data_path


class CollectEngine:
    class Stocks:
        @staticmethod
        def getfulldata(stock_id=""):
            if stock_id in stock_dict:
                f = fe()
                f.delete(stock_id)
                df: pd.DataFrame = ts.get_hist_data(stock_id)
                df.to_csv(g_data_path + "{}.csv".format(stock_id))
            else:
                print(f"【{stock_id}】 is not in the datas.py file!")
                return

        @staticmethod
        def getfulldatabystockid(stock_id: str):
            if stock_id in stock_dict:
                start = stock_dict[stock_id]
                f = fe()
                f.delete(stock_id)
                df: pd.DataFrame = ts.get_hist_data(stock_id, start=start, end=str(datetime.date.today()), ktype='D')
                df.to_csv(g_data_path + "{}.csv".format(stock_id))
            else:
                print(f"【{stock_id}】 is not in the datas.py file!")
                return

        @staticmethod
        def getfulldatabytime(stock_id="", start="", end="", ktype='D'):
            if stock_id in stock_dict:
                f = fe()
                f.delete(stock_id)
                df: pd.DataFrame = ts.get_hist_data(stock_id, start=start, end=end, ktype=ktype)
                df.to_csv(g_data_path + "{}.csv".format(stock_id))
            else:
                print(f"【{stock_id}】 is not in the datas.py file!")
                return

        @staticmethod
        def getohlcvdatabystockid(stock_id: str):
            if stock_id not in stock_dict:
                print(f"【{stock_id}】 is not in the datas.py file!")
                return

            start = stock_dict[stock_id]
            f = fe()
            f.delete(stock_id)
            df: pd.DataFrame = ts.get_hist_data(stock_id, start=start, end=str(datetime.date.today()), ktype='D')[["open", "high", "low", "close", "volume"]]
            # df.to_csv(g_data_path + "{}_ohlcv.csv".format(stock_id))
            return df

