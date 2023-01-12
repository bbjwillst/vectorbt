from utils.CollectEngine import CollectEngine as ce
from utils.AnalyzeEngine import AnalyzeEngine as ae
from strategies.strategy import Strategy as st


if __name__ == "__main__":
    # Save stock data to csv
    stockid = '600980'

    stocks = ce.Stocks()
    stocks.getfulldatabytime(stockid, start='2021-12-22', end='2023-01-12')

    st.SMA(stockid)
    ae.totalreturn(stockid)
