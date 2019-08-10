
import matplotlib.pyplot as plt



DEFAULT_X = []

DEFAULT_Y = []

DEFAULT_COLOR = 'b'

DEFAULT_LINE_WIDTH = 0.5

DEFAULT_X_LABEL = ''

DEFAULT_Y_LABEL = ''



def create(subplot, x = DEFAULT_X, y = DEFAULT_Y, color = DEFAULT_COLOR, width = DEFAULT_LINE_WIDTH, x_label = DEFAULT_X_LABEL, y_label = DEFAULT_Y_LABEL):
	return Plot(subplot, x, y, color, width, x_label, y_label)



class Plot:

	def __init__(self, subplot, x = DEFAULT_X, y = DEFAULT_Y, color = DEFAULT_COLOR, width = DEFAULT_LINE_WIDTH, x_label = DEFAULT_X_LABEL, y_label = DEFAULT_Y_LABEL):
		self._subplot = subplot
		self._x = x
		self._y = y
		self._color = color
		self._width = width


		self.update_coodinates()

		self.set_x_label(x_label)

		self.set_y_label(y_label)


	def subplot(self):
		return self._subplot


	def update_coodinates(self):
		self._subplot.plot(self._x, self._y, self._color, self._width)


	def set_x_y(self, x, y):
		self._x = x
		self._y = y
		self.update_coodinates()


	def x(self):
		return self._x


	def y(self):
		return self._y


	def set_x_label(self, x_label):
		self._x_label = x_label
		self._subplot.set_xlabel(self._x_label)


	def x_label(self):
		return self._x_label


	def set_y_label(self, y_label):
		self._y_label = y_label
		self._subplot.set_ylabel(self._y_label)


	def y_label(self):
		return self._y_label




		
