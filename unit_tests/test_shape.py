
import unittest
import utils.shape.point as point



# PointTest

class PointTest(unittest.TestCase):


	def testInstance(self):
		for m in self._mock():

			x = m[0]
			y = m[1]

			p = point.create(x, y)

			self.assertEqual(p.x(), x)
			self.assertEqual(p.y(), y)


	def testEquality(self):
		for m in self._mock():

			x = m[0]
			y = m[1]

			c = point.create(x, y)

			p = point.Point(x, y)

			self.assertEqual(c, p)


	def _mock(self):
		return [
		(0.0, 0.0),
		(1.0, 1.0),
		(1.5, 1.5),
		(2.0, 2.0),
		(2.5, 2.5),
		(3.0, 3.0)
		]
