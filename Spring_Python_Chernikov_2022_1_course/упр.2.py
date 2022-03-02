#Упражн.2
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.1)
plt.plot(x, x*x-x-6, x, 0*x)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=x*x-x-6,\ f_2(x)=0*x$')
plt.grid(True)
plt.show()