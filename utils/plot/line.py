
from utils.shape import point
from .plot import *



# Line

def create(subplot, color = DEFAULT_COLOR, width = DEFAULT_LINE_WIDTH, x_label = DEFAULT_X_LABEL, y_label = DEFAULT_Y_LABEL):
	return Line(subplot, start, end, color, width, x_label, y_label)



class Line(Plot):

	def __init__(self, subplot, color = DEFAULT_COLOR, width = DEFAULT_LINE_WIDTH, x_label = DEFAULT_X_LABEL, y_label = DEFAULT_Y_LABEL):
		self._start = point.create(0.0, 0.0)
		self._end = point.create(0.0, 0.0)

		Plot.__init__(subplot, [start.x(), end.x()], [start.x(), end.y()], color, width, x_label, y_label)


	def start(self):
		return self._start


	def end(self):
		return self._end


	def set_line(start, end):
		self._start = start
		self._end = end

		self.set_x_y(self, [start.x(), end.x()], [start.x(), end.y()])