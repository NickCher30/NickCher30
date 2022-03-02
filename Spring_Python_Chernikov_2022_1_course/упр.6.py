#Упражнен.6
import numpy as np
import math
import matplotlib.pyplot as plt
x = np.arange(-2, 2.01, 0.01)
a = 3
b = 0.5
y = []
for i in x:
    s = 0
    for n in range(0, 100):
        s += b**n * math.cos(a**n * math.pi * i)
    y.append(s)
plt.plot(x, y)
plt.show()