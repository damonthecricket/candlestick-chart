
import market
import candles



## Main

def main():
	ohlc = candles.load('https://pythonprogramming.net/yahoo_finance_replacement')
	m = market.create("EBAY", ohlc)
	m.show()





if __name__ == "__main__":
	main()