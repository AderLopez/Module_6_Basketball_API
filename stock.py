import yfinance as yf

#define the ticker symbol
# tickerSymbol = name.upper()
tickerSymbol = 'TSLA'

#get gata on this ticker
tickerData = yf.Ticker(tickerSymbol)


#get the historical prices for this ticker
tickerDF = tickerData.history(period = '1d',start='2010-1-1', end ='2020-1-25')


#see your data
print(tickerDF)
