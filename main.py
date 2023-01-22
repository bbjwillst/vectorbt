from utils.CollectEngine import CollectEngine as ce
from utils.AnalyzeEngine import AnalyzeEngine as ae
from strategies.strategy import Strategy as st


if __name__ == "__main__":
    # Save stock data to csv
    stockid = '002124'

    # 600980 start='2021-12-22', end='2023-01-16'
    ce.Stocks.getfulldatabytime(stockid, start='2020-08-18', end='2023-01-16')
    st.SMA(stockid)
    ae.totalreturn(stockid)

