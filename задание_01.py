"""Цель:
1. Ознакомление с методами оценки статических характеристик.
Задание 1. Сгенерировать выборку случайных чисел размером 100 и 1000 для двух распределений – экспоненциального и нормального. Для созданных выборок сделать
следующее:
1. Посчитать выборочное среднее и дисперсию, сравнить с математическим ожиданием соответствующих распределений;
2. Посчитать 0.5 и 0.99 квантили, сравнить с соответствующими теоретическими значениями;
3. Построить гистограмму распределения;
4. Построить функцию распределения случайной величины на основе выборки (на
одном графике показать функции распределения, полученные из выборок разного размера и теоретическую);

Задание 2. Сгенерировать три выборки размера 100, 1000 и 10000 для случайных расстояний между двумя точками, равномерно распределенные в прямоугольнике со 
сторонами 10 и 30.
Получить среднее значение расстояния между точками, построить функцию распределения вероятностей и плотности вероятностей случайных расстояний. Показать разницу 
между соответствующими функциями на одном графике.
К каждому заданию необходимо представить краткое объяснение и скриншот программного кода с результатом выполнения. В конце отчета по лабораторной работе 
сформулировать выводы.."""



# Лабораторная работа №2

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
from scipy.stats import norm




def fun_exp(lambd,x):        # Задание №1
    return 1-np.exp(-lambd*x)


def distance(x1,y1,x2,y2):   # Задание №2
    return np.sqrt((x2-x1)**2+(y2-y1)**2)

def distance_line(number):   # Задание №2
    a=10
    b=30
    distances=[]
    for i in range(number):
        x1=np.random.uniform(0,a)
        y1=np.random.uniform(0,b)

        x2=np.random.uniform(0,a)
        y2=np.random.uniform(0,b)

        distances.append(distance(x1,y1,x2,y2))

    distances.sort()
    return distances



#Задание №1

exp_100=np.random.exponential(1, size=100)
exp_1000=np.random.exponential(1,  size=1000)
norm_100=np.random.normal(0,1,  size=100)
norm_1000=np.random.normal(0,1,  size=1000)

print("Mean for exp_100: ",np.mean(exp_100))
print("Mean for norm_100: ",np.mean(norm_100))
print("Mean for exp_1000: ",np.mean(exp_1000))
print("Mean for norm_1000: ",np.mean(norm_1000))

print("\nVar for exp_100: ",np.var(exp_100))
print("Var for norm_100: ",np.var(norm_1000))
print("Var for exp_1000: ",np.var(exp_1000))
print("Var for norm_1000: ",np.var(norm_1000))

# Задание 1.2

print("\nКвантиль 0.5 для exp_100 = ", np.quantile(exp_100,0.5))
print("Квантиль 0.99 для exp_100 = ", np.quantile(exp_100,0.99))
print("Квантиль 0.5 для exp_1000 = ", np.quantile(exp_100,0.5))
print("Квантиль 0.99 для exp_1000 = ", np.quantile(exp_100,0.99))

print("\nКвантиль 0.5 для norm_100 = ", np.quantile(norm_100,0.5))
print("Квантиль 0.99 для norm_100 = ", np.quantile(norm_100,0.99))
print("Квантиль 0.5 для norm_1000 = ", np.quantile(norm_100,0.5))
print("Квантиль 0.99 для norm_1000 = ", np.quantile(norm_100,0.99))

# задантк 1.3

plt.hist(exp_100, 10)
plt.ylabel('частота')
plt.xlabel('значение')
plt.title('Гистограмма exp_100')
plt.show() 

plt.hist(exp_1000, 10)
plt.ylabel('частота')
plt.xlabel('значение')
plt.title('Гистограмма exp_1000')
plt.show() 

plt.hist(norm_100, 10)
plt.ylabel('частота')
plt.xlabel('значение')
plt.title('Гистограмма norm_100')
plt.show() 

plt.hist(norm_1000, 10)
plt.ylabel('частота')
plt.xlabel('значение')
plt.title('Гистограмма norm_1000')
plt.show() 

#задание 1.4


teory_exp_x=np.linspace(0,10,100)
teory_exp_y=fun_exp(1,teory_exp_x)

exp_100_copy=np.copy(exp_100)
exp_1000_copy=np.copy(exp_1000)

exp_100_copy.sort()
exp_1000_copy.sort()

exp_100_copy_y=np.arange(0.,1.,0.01)
exp_1000_copy_y=np.arange(0.,1.,0.001)

plt.figure(dpi=100)
plt.title("Exp")
plt.plot(teory_exp_x,teory_exp_y, label="teory")
plt.plot(exp_100_copy,exp_100_copy_y, label="teory exp_100")
plt.plot(exp_1000_copy,exp_1000_copy_y, label="teory exp_1000")
plt.legend()
plt.show()


teory_norm_x=np.linspace(0,10,100)
teory_norm_y=fun_exp(1,teory_norm_x)

norm_100_copy=np.copy(norm_100)
norm_1000_copy=np.copy(norm_1000)

norm_100_copy.sort()
norm_1000_copy.sort()

norm_100_copy_y=np.arange(0.,1.,0.01)
norm_1000_copy_y=np.arange(0.,1.,0.001)

plt.figure(dpi=100)
plt.title("Norm")
plt.plot(teory_norm_x,teory_norm_y, label="teory")
plt.plot(norm_100_copy,norm_100_copy_y, label="teory norm_100")
plt.plot(norm_1000_copy,norm_1000_copy_y, label="teory norm_1000")
plt.legend()
plt.show()


#задание 1.5




# Задание №2


x_100=distance_line(100)
x_1000=distance_line(1000)
x_10000=distance_line(10000)

aver_100=np.average(x_100)
aver_1000=np.average(x_1000)
aver_10000=np.average(x_10000)

x_100_copy=np.copy(x_100)
x_100_copy.sort()
x_100_copy_y=np.arange(0.,1.,0.01)

x_1000_copy=np.copy(x_1000)
x_1000_copy.sort()
x_1000_copy_y=np.arange(0.,1.,0.001)

x_10000_copy=np.copy(x_10000)
x_10000_copy.sort()
x_10000_copy_y=np.arange(0.,1.,0.0001)


plt.figure(dpi=100)
plt.title(" Функция распределения вероятностей")
plt.plot(x_100_copy,x_100_copy_y, label="x_100")
plt.plot(x_1000_copy,x_1000_copy_y, label="x_1000")
plt.plot(x_10000_copy,x_10000_copy_y, label="x_10000")
plt.legend()
plt.show()


dist_100 = norm(loc=np.mean(x_100), scale=np.std(x_100))
x_100_d = np.linspace(dist_100.ppf(0.001),
                dist_100.ppf(0.999), 100)

dist_1000 = norm(loc=np.mean(x_1000), scale=np.std(x_1000))
x_1000_d = np.linspace(dist_1000.ppf(0.001),
                dist_1000.ppf(0.999), 1000)

dist_10000 = norm(loc=np.mean(x_1000), scale=np.std(x_1000))
x_10000_d = np.linspace(dist_10000.ppf(0.001),
                dist_1000.ppf(0.999), 10000)

plt.figure(dpi=100)
plt.plot(x_100,dist_100.pdf(x_100_d), label='PDF 100')
plt.plot(x_1000,dist_1000.pdf(x_1000_d), label='PDF 1000')
plt.plot(x_10000,dist_10000.pdf(x_10000_d), label='PDF 10000')
plt.title('Функция плотности вероятностей')
plt.legend()
plt.show()

