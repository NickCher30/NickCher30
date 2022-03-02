Упражнен.3
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.1)
y = np.log((x**2+1)*(np.exp(-abs(x)/10)), (1+np.tan(1/(1+(np.sin(x))**2))))
plt.plot(x, y)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x)=y$')
plt.grid(True)
plt.show()
