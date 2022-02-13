#Упражнен.5
import numpy as np
import matplotlib.pyplot as plt
x = [1, 1.65, 2, 2.6, 3, 4, 4.3, 5, 5.25, 6, 6.4]
y = [1, 1.42, 1.1, 2, 1.2, 2.5, 2.7, 2.1, 1.75, 3.1, 2.2]
p, v = np.polyfit(x, y, deg=9, cov=True)
p_f = np.poly1d(p)
y_y = p_f(x)
plt.plot(x, y_y, x, y)
plt.errorbar(x, y, xerr=0.065, yerr=0.065)
plt.grid()
plt.show()