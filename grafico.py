from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 2 + 1

plt.plot(x, y, '-r', label='y = x² + 1')
plt.title('Gráfico de y = x² + 1')
plt.xlabel('Eixo x', color='#1C2833')
plt.ylabel('Eixo y', color='#1C2833')
plt.legend(loc='upper center')
plt.grid()

plt.show()
