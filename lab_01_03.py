# Задание 3

import matplotlib.pyplot as plt
from scipy.stats import uniform 
import random

inf = 0
sup = int(input("Введите размер стороны квадрата:  "))

x = random.uniform(inf, sup)
y = random.uniform(inf, sup)

print(x,y)
plt.scatter(x,y)
plt.axis([0, sup, 0, sup])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()

