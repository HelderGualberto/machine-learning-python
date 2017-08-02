import matplotlib.pyplot as plt
import numpy as np


s = np.array([100,400,324,546,134])
s2 = np.array([423,543,134,521,355])


plt.plot(s, c="Red", ls="--", marker="^", ms="5", label='Salario Helder') #Adiciona elementos no gráfico
plt.plot(s2, c="Blue", marker="s", ms="5", label='Salario Andressa') #Adiciona elementos no gráfico
plt.legend(loc="upper left")
plt.show() #Plota o gráfico


