# Задание 2

import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 

np.random.seed(2016) # replicar random

# parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})



N, p = 30, 0.4 # parametros de forma 
binomial = stats.binom(N, p) # Distribución

# histograma
aleatorios = binomial.rvs(1000)  # genera aleatorios
cuenta = plt.hist(aleatorios, 20)
plt.ylabel('частота')
plt.xlabel('значение')
plt.title('Биномиальная Гистограмма')
plt.show()


print( "\n",len(aleatorios), " случайных чисел с биномиальным распределением\n", aleatorios)
print("\n Дисперсия\n", np.var(aleatorios))
print("\n Математическое ожидание\n", np.mean(aleatorios))
