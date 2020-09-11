# Zenya Koprowski
# FE 550 Homeowrk 1
# I used this website as a resource for help: https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 2 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
tan_x = np.linspace(-2*np.pi, 2*np.pi, 1000)
tan_y = np.tan(tan_x)
plt.title("Plot of Sine, Tan, Cosine Graph")
plt.plot(x, y_sin, label = "Sine Graph")
plt.plot(x, y_cos, label = "Cosine Graph")
plt.plot(tan_x, tan_y, label = "Tan Graph")
plt.legend(loc = "lower left")
plt.ylim([-1,1])
plt.xlim([0,6])
plt.show()
