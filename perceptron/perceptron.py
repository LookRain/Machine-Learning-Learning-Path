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
  truth = []

  # for ind, item in enumerate(x):
  #   x[ind] = random.uniform(0, 10)

  for i in range(50):
    x.append(random.uniform(0, 10))
    y.append(random.uniform(10, 20))
    truth.append(1)

  for j in range(50, 100):
    x.append(random.uniform(10, 20))
    y.append(random.uniform(0, 10))
    truth.append(0)

  weights = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]

  iteration = 0
  # print(cal_output(0, [1,2,3], 1, 2))
  local_error = 0
  global_error = 0
  output = 0
  while(True):
    iteration += 1

    for ind in range(NUM_INSTANCES):
      output = cal_output(theta, weights, x[ind], y[ind])
      local_error = truth[ind] - output
      print(local_error)



    # if (test == 10):
    #   break
    # test += 1
    # print(test)


  



  plt.plot(x, y, 'ro')
  plt.axis([0, 20, 0, 20])

  plt.show()

def cal_output(t, w, x, y):
  sum = x * w[0] + y * w[1] + w[2]
  if (sum >= t):
    return 1
  else:
    return 0


main()

