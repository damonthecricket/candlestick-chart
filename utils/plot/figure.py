
import matplotlib.pyplot as plt
import utils.plot as plot



DEFAULT_TITLE = "Figure"



def create(title = DEFAULT_TITLE):
	return Figure(title)



class Figure:

	def __init__(self, title = DEFAULT_TITLE):
		self._figure = plt.figure(num = title)
		self._title = title


	def figure(self):
		return self._figure


	def title(self):
		return self._title


	def subplot(self, nrows, ncols, index):
		ax = self._figure.add_subplot(nrows, ncols, index)
		return plot.create(ax)


	def show(self):
		plt.show(self._figure)
		

