
from model.stock import Stock
from model.candle import Candle

import matplotlib.pyplot as plt



## Stock

def stock(stock):
	fgr = plt.figure(1)

	ax = fgr.add_subplot(1, 1, 1)

	ax.set_xlabel('date')
	ax.set_ylabel('price')

	x = [1, 2, 3, 4, 5, 6, 7]
	y = [1, 2, 3, 4, 5, 6, 7]

	ax.plot(x, y, 'b', linewidth = 0.5)

	plt.xticks(x, ['a', 'b', 'c', 'd'])
	plt.yticks(y, y)
	plt.title("Name")
	plt.show(fgr)
	
	
	
	
	