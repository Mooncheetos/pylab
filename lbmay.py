import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 2, 100)
y = lambda x: 3 * x**4 - 12 * x + 9
plt.plot(x, y(x), color="k", linewidth=2.5)
plt.plot([-10, 10], [0, 0], color="k", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.savefig("lab.pdf", bbox_inches="tight")
plt.show()
