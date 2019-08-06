
import unittest

import model, model.stock
from model.candle import *

import db



## TestStock

class TestStock(unittest.TestCase):
	
	def test_instance(self):
		for file_path in stock_mock():

			csv = db.load_csv(file_path)

			name = db.file_name_from_path(file_path)

			candles = []

			for c in csv:

				candle = Candle(c)

				candles.append(candle)

			loaded = model.stock.load(file_path)
			created = model.stock.create(name, csv)
			stock = model.stock.Stock(name, csv)

			self.assertEqual(loaded.name(), name)
			self.assertEqual(loaded.candles(), candles)

			self.assertEqual(created.name(), name)
			self.assertEqual(created.candles(), candles)

			self.assertEqual(stock.name(), name)
			self.assertEqual(stock.candles(), candles)




## TestCandle

class TestCandle(unittest.TestCase):
	
	def test_instance(self):
		for file_path in stock_mock():

			csv = db.load_csv(file_path)

			self.assertTrue(len(csv) != 0)

			candle_count = 0

			for c in csv:

				candle_count += 1

				candle = Candle(c)

				self.assertEqual(candle.date(), c[db.DATE_KEY])
				self.assertEqual(candle.open(), c[db.OPEN_KEY])
				self.assertEqual(candle.high(), c[db.HIGH_KEY])
				self.assertEqual(candle.low(), c[db.LOW_KEY])
				self.assertEqual(candle.close(), c[db.CLOSE_KEY])
				self.assertEqual(candle.volume(), c[db.VOLUME_KEY])
				self.assertEqual(candle.open_int(), c[db.OPEN_INT_KEY])


			self.assertEqual(candle_count, len(csv))


def stock_mock():
	return [ "data/aa.us.txt", "data/aa.us.txt", "data/aaap.us.txt" ]


	