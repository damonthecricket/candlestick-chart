
import model.stock as stock
import plot.stock as plot
import db



## Main

def main():
	print("Plot ...")

	stc = stock.load("data/a.us.txt")

	plt = plot.Plot(stc)
	
	plt.draw()




if __name__ == "__main__":
	main()