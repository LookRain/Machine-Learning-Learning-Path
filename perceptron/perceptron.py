import numpy as np
import matplotlib.pyplot as plt
import random
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

MAX_ITER = 100
LEARNING_RATE = 0.1
NUM_INSTANCES = 100
theta = 0
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()

def main():
	x = []
	y = []

	truth = np.zeros(NUM_INSTANCES)

	# for ind, item in enumerate(x):
	# 	x[ind] = random.uniform(0, 10)

	for i in range(50):
		x.append(random.uniform(0, 10))
		y.append(random.uniform(10, 20))

	for j in range(50, 100):
		x.append(random.uniform(10, 20))
		y.append(random.uniform(0, 10))

	print(len(x))

	# for item in enumerate(y):
	# 	y[ind] = random.uniform(10, 20)
	
	# sampl = np.random.uniform(low=0.5, high=13.3, size=(50,))



	plt.plot(x, y, 'ro')
	plt.axis([0, 20, 0, 20])

	plt.show()
	# print(data_points)

main()