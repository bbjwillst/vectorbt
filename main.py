from utils.CollectEngine import CollectEngine as ce
from utils.AnalyzeEngine import AnalyzeEngine as ae
from strategies.strategy import Strategy as st


if __name__ == "__main__":
    # Save stock data to csv
    # stocks = ce.Stocks()
    # stocks.getfulldatabytime("600980", start='2021-12-22', end='2023-01-12')

    # st.SMA('600980')
    ae.totalreturn("600980")
