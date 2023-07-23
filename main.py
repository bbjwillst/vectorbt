from utils import FileExt
from utils.CollectEngine import CollectEngine as ce
from utils.AnalyzeEngine import AnalyzeEngine as ae
from strategies.strategy import Strategy as st
import datetime

if __name__ == "__main__":
    # Save stock data to csv
    stockid = '159992'

    # ce.Stocks.getfulldatabystockid(stockid)
    # st.SMA(stockid)
    # # st.SMARSI(stockid)
    # ae.totalreturn(stockid)

    # st.MA(stockid)

    # delete all files
    fe = FileExt.FileExt()
    fe.deleteallfiles()