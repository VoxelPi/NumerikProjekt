import numpy as np
import matplotlib.pyplot as plt

from quad2d import quadTriangle

# Define reference triangle.
z = np.array([[0, 0], [1, 0], [0, 1]])

# Approximate the integral.
def approximate(f, n):
    xs, ws = quadTriangle(n, z)
    return sum([f(x)*w for (x,w) in zip(xs,ws)])

# Plot the error
def plot_error(n, f, expected, label):
    approx = np.array([approximate(f, i) for i in n])

    plt.plot(n**2, approx - expected, label=label)

# Create the plot.
n = np.arange(1, 5+1, 1)
plt.figure()

f_expected = 1
f = lambda x : np.exp(x[0] + x[1])
plot_error(n, f, f_expected, "$\exp(x + y)$")

g_expected = 2/5
g = lambda x : np.sqrt(x[0] + x[1])
plot_error(n, g, g_expected, "$\sqrt{x + y}$")

plt.xlabel("Anzahl der Funktionsauswertungen n")
plt.xticks(n**2)
plt.ylabel("Quadraturfehler")
plt.title("Quadraturfehler")
plt.legend()
plt.grid()
plt.show()
