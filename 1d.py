import numpy as np
import matplotlib.pyplot as plt

def y(C, p, x):
    return C * x**p

x1 = np.linspace(1, 1000)
y1 = y(1, 1, x1)

x2 = np.linspace(1, 1000)
y2 = y(10, 1, x1)

x3 = np.linspace(1, 1000)
y3 = y(10, 2, x1)

plt.figure()
plt.xlim([1,1000])
plt.ylim([1,10**7])
plt.loglog(x3, y3, label="$y = 10 \\cdot x^2$")
plt.loglog(x2, y2, label="$y = 10 \\cdot x^1$")
plt.loglog(x1, y1, label="$y =  1 \\cdot x^1$")
plt.legend()
plt.grid()
plt.axhline(1, color="black")
plt.xlabel("x")
plt.ylabel("y")
plt.title("log-log Plot")
plt.gcf().set_dpi(150.0)
plt.show()