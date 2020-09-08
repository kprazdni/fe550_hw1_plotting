# Zenya Koprowski
# FE 550 Homeowrk 1
# I used this website as a resource for help: https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.title("Plot of Sine and Cosine Graph")
plt.plot(x, y_sin, label = "Sine Graph")
plt.plot(x, y_cos, label = "Cosine Graph")
plt.legend(loc = "lower left")
plt.show()

