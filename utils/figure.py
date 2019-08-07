
import matplotlib.pyplot as plt



DEFAULT_TITLE = "Figure"



def create(title = DEFAULT_TITLE):
	return Figure(title)



class Figure:

	def __init__(self, title = DEFAULT_TITLE):
		self._figure = plt.figure(num = title)
		self._title = title


	def figure(self):
		return self._figure


	def title(self):
		return self._title


	def add_subplot(a = 1, b = 1, c = 1):
		return self._figure.add_subplot(a, b, c)


	def show(self):
		plt.show(self._figure)
		


## Stock

def stock(stock):
	fgr = plt.figure(1)

	ax = fgr.add_subplot(1, 1, 1)

	ax.set_xlabel('date')
	ax.set_ylabel('price')

	x = [1, 2, 3, 4, 5, 6, 7]
	y = [1, 2, 3, 4, 5, 6, 7]

	ax.plot(x, y, 'b', linewidth = 0.5)

	plt.xticks(x, ['a', 'b', 'c', 'd'])
	plt.yticks(y, y)
	plt.title("Name")
	plt.show(fgr)
	
	
	
	
	