import numpy as np
import matplotlib.pyplot as plt
import random

MAX_ITER = 100
LEARNING_RATE = 0.1
NUM_INSTANCES = 100
theta = 0


def graph(formula, x_range, c, l):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y, c, label=l)  
    

def main():
  x = []
  y = []
  truth = []

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

  local_error = 0
  global_error = 0
  output = 0
  
  while(True):
    iteration += 1
    global_error = 0

    for ind in range(NUM_INSTANCES):
      output = cal_output(theta, weights, x[ind], y[ind])
      local_error = truth[ind] - output

      weights[0] += LEARNING_RATE * local_error * x[ind]
      weights[1] += LEARNING_RATE * local_error * y[ind]
      weights[2] += LEARNING_RATE * local_error
      global_error += (local_error * local_error)

    print("RMS Error: %n", global_error)
    equation = "-({}/{})*x-{}/{}"
    final_equation = equation.format(weights[0], weights[1], weights[2], weights[1])
    graph(final_equation, range(0,20), 'aqua', iteration)
    if (global_error == 0 or iteration > MAX_ITER):
      break

  str = "{}*x + {}*y + {} = 0"
  print(str.format(weights[0], weights[1], weights[2]))
  equation = "-({}/{})*x-{}/{}"
  final_equation = equation.format(weights[0], weights[1], weights[2], weights[1])
  print(final_equation)
  graph(final_equation, range(0,20), 'red', 'final')

  plt.plot(x, y, 'ro')
  plt.axis([0, 20, 0, 20])
  plt.legend()
  plt.show()


def cal_output(t, w, x, y):
  sum = x * w[0] + y * w[1] + w[2]
  if (sum >= t):
    return 1
  else:
    return 0


main()

