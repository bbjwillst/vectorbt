from utils.CollectEngine import CollectEngine as ce


if __name__ == "__main__":
    # Save stock data to csv
    stocks = ce.Stocks()
    stocks.getFullDataByTime("600980", start='2021-12-22', end='2022-12-01')



