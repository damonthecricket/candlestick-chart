
import db



# Candle

def create(dictionary):
	return Candle(dictionary)



class Candle:

	def __init__(self, dictionary):
		self._date = dictionary[db.DATE_KEY] 
		self._open = dictionary[db.OPEN_KEY] 
		self._high = dictionary[db.HIGH_KEY] 
		self._low = dictionary[db.LOW_KEY] 
		self._close = dictionary[db.CLOSE_KEY] 
		self._volume = dictionary[db.VOLUME_KEY] 
		self._open_int = dictionary[db.OPEN_INT_KEY] 


	def date(self):
		return self._date


	def open(self):
		return self._open


	def high(self):
		return self._high


	def low(self):
		return self._low


	def close(self):
		return self._close


	def volume(self):
		return self._volume


	def open_int(self):
		return self._open_int


	def is_bullish(self):
		return self._low < self._high


	def is_bearish(self):
		return self._low > self._high


	def is_unit(self):
		return self._low == self._high


	def current(self):
		if self.is_bullish():
			return self._high
		elif self.is_bearish():
			return self._low
		else:
			return self._high


	def __eq__(self, other):
		return self._date == other.date() and self._open == other.open() and self._high == other.high() and \
				self._low == other.low() and self._close == other.close() and self._volume == other.volume() and \
				self._volume == other.volume() and self._open_int == other.open_int() 


	def __str__(self):
		return "Japan candle, data: %s, open: %s, high: %s, low: %s, close: %s, volume: %s, open int: %s" % \
							(self._date, self._open, self._high, self._low, self._close, self._volume, self._open_int)


							