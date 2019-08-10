
from model.stock import Stock
from model.candle import Candle

import matplotlib.pyplot as plt
	

	
	
class Plot:

	def __init__(self, stock, x_label = 'Date', y_label = 'Price'):
		self._stock = stock
		self._figure = plt.figure(1)
		self._x_label = x_label
		self._y_label = y_label


	def draw(self):
		ax = self._figure.add_subplot(1, 1, 1)

		ax.set_xlabel(self._x_label)

		ax.set_ylabel(self._y_label)

		x = [1, 2, 3, 4, 5, 6, 7]
		y = [1, 2, 3, 4, 5, 6, 7]

		ax.plot(x, y, 'b', linewidth = 0.5)

		plt.xticks(x, ['a', 'b', 'c', 'd'])

		plt.yticks(y, y)

		plt.title(self._stock.name())

		plt.show(self._figure)
			
