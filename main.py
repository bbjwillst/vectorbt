from utils.CollectEngine import CollectEngine as ce
from strategies.strategy import Strategy as st


if __name__ == "__main__":
    # Save stock data to csv
    # stocks = ce.Stocks()
    # stocks.getfulldatabytime("600980", start='2021-12-22', end='2022-12-07')

    st.SMA('600980')

