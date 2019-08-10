
import unittest

import db
import utils.csv as csv
import utils.folder as folder

# from db import folder_content



## TestDB

class TestDB(unittest.TestCase):

	def test_load(self):
		f = "unit_tests/data"
		db_content = db.load(f)

		folder_content = []

		for p in self.__db_paths_mock():
			c = csv.load(p)
			folder_content.append(c)

		self.assertEqual(db_content, folder_content)


	def __db_paths_mock(self):
		return ["unit_tests/data/1.txt",
				"unit_tests/data/2.txt",
				"unit_tests/data/3.txt"
				]

