import math
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(18073782)

iter = 500
N = np.arange(1, 500, 1)


def makeEstimate(i):  # Running Monte Carlo Simulation
    sq, cr = [0, 0]
    for j in range(1, i + 1):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            cr += 1
        sq += 1
    return 4 * cr / sq


def calculatePi():  # Main function to calculate value of pi
    P = []
    for i in N:
        sum = 0
        for j in range(iter):
            sum += makeEstimate(i)
        P.append(sum / iter)

    Y = np.zeros(len(N))
    Y[:] = math.pi

    plt.plot(N, P, label='Simulation')
    plt.plot(N, Y, label='Actual Value')
    plt.xlabel('No. of pebbles')
    plt.ylabel('Value of PI')
    plt.legend(loc='upper right')
    plt.show()


calculatePi()
