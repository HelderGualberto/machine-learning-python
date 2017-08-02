import numpy as np
import matplotlib.pyplot as plt



iris_data = np.genfromtxt('../data/iris.data',delimiter=',',usecols=(0,1,2,3),unpack=True)
print(iris_data)

iris_setosa_sepal = iris_data[0,:50]
iris_versicolor_sepal = iris_data[0,50:100]
iris_virginica_sepal = iris_data[0,100:]

plt.plot(iris_setosa_sepal, c='Red',label='Comp.Sepala iris Setosa', ls=':')
plt.plot(iris_versicolor_sepal, c='Blue',label='Comp.Sepala iris Versicolor', ls=':')
plt.plot(iris_virginica_sepal, c='Green',label='Comp.Sepala iris Virginica', ls=':')
plt.legend(loc="upper right")
plt.show()