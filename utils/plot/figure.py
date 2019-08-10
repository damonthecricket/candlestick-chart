
import matplotlib.pyplot as plt
from . import plot
from . import line
from . import axe



DEFAULT_TITLE = "Figure"



def create(title = DEFAULT_TITLE):
	return Figure(title)



class Figure:

	def __init__(self, title = DEFAULT_TITLE):
		self._figure = plt.figure(num = title)
		self._title = title

		self._x_axe = None
		self._y_axe = None


	def figure(self):
		return self._figure


	def title(self):
		return self._title


	def subplot(self, nrows, ncols, index):
		ax = self._figure.add_subplot(nrows, ncols, index)
		return plot.create(ax)


	def line(self, nrows, ncols, index):
		ax = self._figure.add_subplot(nrows, ncols, index)
		return line.create(ax)


	def set_x_axe(self, axe):
		self._x_axe = axe


	def x_axe(self):
		return self._x_axe


	def set_y_axe(self, axe):
		self._y_axe = axe


	def y_axe(self):
		return self._y_axe


	def show(self):
		if self._x_axe is not None:
			plt.xticks(self._x_axe.ticks(), self._x_axe.values())

		if self._y_axe is not None:
			plt.yticks(self._y_axe.ticks(), self._y_axe.values())
			
		plt.show(self._figure)
		

