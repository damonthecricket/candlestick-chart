
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc



# Market

def create(name, candles):
	return Market(name, candles)



class Market:


	def __init__(self, name, candles):
		self._name = name
		self._candles = candles
	

	def show(self):
		fig = plt.figure()
		ax1 = plt.subplot2grid((1,1), (0,0))

		for label in ax1.xaxis.get_ticklabels():
			label.set_rotation(45)

		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
		ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
		ax1.grid(True)

		candlestick_ohlc(ax1, self._candles, width = 0.4, colorup = '#77d879', colordown = '#db3f3f')
    
    
		plt.xlabel('Date')
		plt.ylabel('Price')
		plt.title(self._name)
		plt.legend()
		plt.subplots_adjust(left = 0.09, bottom = 0.20, right = 0.94, top = 0.90, wspace = 0.2, hspace = 0)
		plt.show()


