
from model.candle import *
from db import load_csv, file_name_from_path



# Stock

def load(path):
	csv = load_csv(path)
	name = file_name_from_path(path)
	return Stock(name, csv)



def create(name, csv):
	return Stock(name, csv)



class Stock:

	def __init__(self, name, csv):
		self._name = name

		self._candles = []

		for c in csv:
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



		