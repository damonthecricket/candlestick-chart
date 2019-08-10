


# Constants

DEFAULT_X = 0.0

DEFAULT_Y = 0.0



# Point

def create(x = DEFAULT_X, y = DEFAULT_Y):
	return Point(x, y)



class Point:

	def __init__(self, x = DEFAULT_X, y = DEFAULT_Y):
		self._x = x
		self._y = y


	def set_x(self, x):
		self._x = x


	def x(self):
		return self._x


	def set_y(self, y):
		self._y = y


	def y(self):
		return self._y


	def __eq__(self, other):
		return self._x == other.x() and self._y == other.y()


	def __str__(self):
		return "Point class, x %s, y %s" % (self._x, self._y)


		