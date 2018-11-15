import numpy as np
from matplotlib import *
from PIL import Image

filename = 'robot.jpg'

def main():
	image = Image.open(filename).convert('L')
	image = np.array(image)

	pyplot.plot(image)
	pyplot.show()


main()