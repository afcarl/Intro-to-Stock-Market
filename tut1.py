import pandas_datareader as web
import datetime
import candlestick as cd

def main():
    start = datetime.datetime(2016,1,1)
    end = datetime.date.today()
    apple = web.DataReader("AAPL","yahoo",start,end)
    print(type(apple))
    print(apple.head())

    cd.pandas_candlestick_ohlc(apple)

if __name__ == "__main__":
    main()