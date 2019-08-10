
import utils.file as file
import utils.csv as csv

from model.candle import *



# Stock

def load(path):
	c = csv.load(path)
	name = file.name_from_path(path)
	return Stock(name, c)



def create(name, csv_file):
	return Stock(name, csv_file)



class Stock:

	def __init__(self, name, csv_file):
		self._name = name

		self._candles = []

		for c in csv_file:
			self._candles.append( Candle(c) )


		self._dates = []

		for candle in self._candles:
			self._dates.append(candle.date)


	def name(self):
		return self._name


	def candles(self):
		return self._candles


	def dates(self):
		return self._dates


	def __eq__(self, other):
		return self._name == other.name() and self._candles == other.candles()


	def __str__(self):
		return "Stock, name: %s, candles: %s" % (self._name, self._candles)



		