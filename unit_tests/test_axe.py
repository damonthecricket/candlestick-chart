
import unittest
import utils.plot.axe as axe



# TestAxe

class TestAxe(unittest.TestCase):

	def test_instance(self):
		for m in self._mock():
			ticks = m[0]
			values = m[1]

			a = axe.create(ticks, values)

			self.assertEqual(a.ticks(), ticks)
			self.assertEqual(a.values(), values)


	def test_equality(self):
		for m in self._mock():
			ticks = m[0]
			values = m[1]

			created = axe.create(ticks, values)
			a = axe.Axe(ticks, values)

			self.assertEqual(created, a)


	def _mock(self):
		return [
		(2, ["1", "2"]),
		(3, ["one", "two", "three"]),
		(4, ["four", "three", "two", "one"])
		]