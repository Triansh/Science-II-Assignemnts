import matplotlib.pyplot as plt
import numpy as np
import random
import math

random.seed(1823078)


def plot(X, Y, A, xlab, ylab):  # helper function for plotting
    plt.plot(X, A, label='Analytical')
    plt.plot(X, Y, label='Simulation')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend(loc='upper right')
    plt.show()


iter = 10000
maxN = 100
N = np.arange(1, maxN + 1, 1)


def nCr(n, r):  # calculation of nCr
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def prob(n):  # calculation of probability
    c = nCr(2 * n, n)
    p = 2 ** (2 * n)
    return c / p


def move():  # helper function for deciding to move left or right
    return 1 if random.random() >= 0.5 else -1


def meanSquare():  # calculation of mean square displacement
    M = []
    for i in N:
        tot = 0
        for j in range(iter):
            sum = 0
            for k in range(i):
                sum += move()
            tot += sum ** 2
        tot /= iter
        M.append(tot)

    plot(N, M, N, 'No. of steps', 'Mean Square Displacement')


def mean():  # calculation of mean displacement
    M = []
    for i in N:
        tot = 0
        for j in range(iter):
            sum = 0
            for k in range(i):
                sum += move()
            tot += sum
        tot /= iter
        M.append(tot)

    plot(N, M, np.zeros((maxN)), 'No. of steps', 'Mean Displacement')


def twoRandomWalk():  # calculation of two people meeting at same place after n steps

    ST = []
    for i in range(1, maxN + 1):
        ST.append(prob(i))

    M = []
    for i in N:
        tot = 0
        for j in range(iter):
            sum1, sum2 = [0, 0]
            for k in range(i):
                sum1 += move()
                sum2 += move()
            tot += int(sum1 == sum2)
        tot /= iter
        M.append(tot)

    plot(N, M, ST, 'No. of steps', 'Probability of meeting')


def getBellCurve():  # Histogram (Bell Curve) for displacement

    bins = np.arange(-maxN, maxN + 2, 1)
    B = []
    for i in range(iter * 50):
        sum1, sum2 = [0, 0]
        for k in range(maxN):
            sum1 += move()
            sum2 += move()
        B.append(sum1 - sum2)

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.hist(B, bins=bins)
    ax.set_xlabel('Displacement of person')
    ax.set_ylabel('Frequency of possible displacements')
    plt.show()


def originMeeting():  # calculation of reaching back to origin after n steps
    X = np.arange(0, maxN + 1, 1)

    ST = []
    for i in range(0, maxN + 1, 1):
        ST.append(0 if i % 2 == 1 else prob(i // 2))

    M = []
    for i in X:
        tot = 0
        for j in range(iter):
            sum = 0
            for k in range(i):
                sum += move()
            tot += int(sum == 0)
        M.append(tot / iter)

    plot(X, M, ST, 'No. of steps', 'Probability of reaching origin')


mean()
meanSquare()
twoRandomWalk()
getBellCurve()
originMeeting()
