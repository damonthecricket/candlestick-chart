
import utils.figure as figure
import utils.plot as plot
import db



## Main

def main():
	print("Plot ...")

	f = figure.create("Stock")
	ax = f.subplot(1, 1, 1)
	ax.set_x_y([0, 1, 2, 3], [0, 1, 2, 3])
	ax.set_x_label('x')
	ax.set_y_label('Y')
	f.show()




if __name__ == "__main__":
	main()