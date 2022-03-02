import numpy as np
import matplotlib.pyplot as plt
data = [16, 18, 20, 22, 24]
plt.title('Опрос', size=20)
plt.pie(data, labels=('А.', 'Б.', 'В.', 'Г.', 'Д.'))
plt.show()


import numpy as np
import matplotlib.pyplot as plt
data = [20, 20, 18, 22, 20]
plt.title('Опрос', size=20)
plt.pie(data, labels=('А.', 'Б.', 'В.', 'Г.', 'Д.'))
plt.show()




import numpy as np
import matplotlib.pyplot as plt
data = [24, 22, 20, 18, 16]
plt.title('Опрос', size=20)
plt.pie(data, labels=('А.', 'Б.', 'В.', 'Г.', 'Д.'))
plt.show()






import matplotlib.pyplot as plt
colors = ['white', 'pink', 'red', 'green', 'yellow']
labels = ['А.', 'Б.', 'В.', 'Г.', 'Д.']
x = [1, 2, 3, 4, 5]
y = [16, 18, 20, 22, 24]
plt.ylabel('Количество опрошенных')
plt.title('Опрос')
plt.bar(x, y, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')
plt.show()




import matplotlib.pyplot as plt
colors = ['white', 'pink', 'red', 'green', 'yellow']
labels = ['А.', 'Б.', 'В.', 'Г.', 'Д.']
x = [1, 2, 3, 4, 5]
y = [20, 20, 18, 22, 20]
plt.ylabel('Количество опрошенных')
plt.title('Опрос')
plt.bar(x, y, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')
plt.show()



import matplotlib.pyplot as plt
colors = ['white', 'pink', 'red', 'green', 'yellow']
labels = ['А.', 'Б.', 'В.', 'Г.', 'Д.']
x = [1, 2, 3, 4, 5]
y = [24, 22, 20, 18, 16]
plt.ylabel('Количество опрошенных')
plt.title('Опрос')
plt.bar(x, y, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')
plt.show()



#круговые диаграммы - если нам необязательно знать точный модуль значений информации, привычнее
#столбчатые - легче сравнивать, точнее видны данные(показатели-числа на оси ординат), нагляднее.
#итак, столбчатые диаграммы нагляднее