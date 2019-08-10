


# Axe

def create(ticks, values):
	return Axe(ticks, values)



class Axe:

	def __init__(self, ticks, values):
		self._ticks = ticks
		self._values = values


	def ticks(self):
		return self._ticks


	def values(self):
		return self._values


	def __eq__(self, other):
		return self._ticks == other.ticks() and self._values == other.values()


	def __str__(self):
		return "Axe class, ticks %s, values %s" % (self._ticks, self._values)
		