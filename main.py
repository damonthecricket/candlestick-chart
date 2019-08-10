
import utils.plot.axe as axe
import utils.plot.figure as figure
import utils.plot.plot as plot
import db



## Main

def main():
	print("Plot ...")

	f = figure.create("Stock")

	sp = f.subplot(1, 1, 1)
	sp.set_x_y([0,  3], [0, 3])
	sp.set_x_label('x')
	sp.set_y_label('Y')

	x_axe = axe.create([1, 2], ["September", "November"])
	y_axe = axe.create([1, 2], ["10$", "1000$", "10000$"])

	f.set_x_axe(x_axe)
	f.set_y_axe(y_axe)

	f.show()




if __name__ == "__main__":
	main()