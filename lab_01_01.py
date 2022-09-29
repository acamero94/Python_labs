# Задание 1 

import matplotlib.pyplot as plt
from scipy.stats import uniform 

a, b = 1 , 10
c, d = 1 , 10
x = uniform .rvs(a, b, size = 10) 
y = uniform .rvs(c, d, size = 10)
print("\n Matriz 10*2\n")
for i in range(10):
    print(x[i], "    ", y[i], "\n")


plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()
