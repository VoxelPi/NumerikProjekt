import numpy as np
import matplotlib.pyplot as plt

from quad2d import quadTriangle

z = np.array([[0, 0], [1, 0], [0, 1]])

# def f(x):
#     return np.exp(x[0] + x[1])

def f(x):
    return np.sqrt(x[0] + x[1])

def approximate(n):
    (x, w) = quadTriangle(n, z)
    sum = 0
    for i in range(n**2):
        sum += w[i] * f(x[i])
    return sum

n = np.arange(1, 11, 1)
approx = np.vectorize(approximate)(n)

plt.figure()
plt.plot(n, approx)
plt.xlabel("n")
plt.ylabel("approximation")
plt.title("$f(x,y) = \sqrt{x + y}$")
plt.grid()
plt.show()