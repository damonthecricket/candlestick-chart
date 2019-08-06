
import unittest

import db
from db import folder_content, load_csv



## TestDB

class TestDB(unittest.TestCase):

	def test_load(self):
		folder = "unit_tests/data"
		db_content = db.load(folder)

		folder_content = []

		for p in self.__db_paths_mock():
			csv = load_csv(p)
			folder_content.append(csv)

		self.assertEqual(db_content, folder_content)


	def __db_paths_mock(self):
		return ["unit_tests/data/1.txt",
				"unit_tests/data/2.txt",
				"unit_tests/data/3.txt"
				]

