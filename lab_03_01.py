"""

Лабораторная работа №3
Исследование распределений и моментов связанных
с преобразованием случайных величин
Цель:
1. Применение распределений для преобразования случайных величин.
Задание. Сгенерировать выборку точек, равномерно распределенных внутри круга двумя способами:
1. Равномерно распределить точки внутри квадрата, внутрь которого вписана окружность, и отфильтровать точки, лежащие за пределами окружности.
2. Генерировать точки путем задания случайного угла и расстояния от центра окружности. Радиус окружности R=10, размер выборки 1000 точек.
Для созданных выборок сделать следующее:
1. Создать рисунок, иллюстрирующий расположение точек сгенерированной выборки внутри окружности;
2. Найти выборочные средние координат точек и их дисперсию;
3. Построить график плотности распределения расстояния от случайной равномерно распределенной точки в круге до фиксированной точки лежащей вне окружности
(к примеру, с координатами X=20, Y=0).
4. Построить график плотности распределения расстояния между двумя случайными точками, равномерно расположенными внутри круга. К каждому заданию необходимо представить краткое объяснение и скриншот
программного кода с результатом выполнения.
В конце отчета по лабораторной работе сформулировать выводы. 


"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

circle_radius = 10
set_size = 1000

set_x = []
set_y = []
dots_counter = 0
while dots_counter < set_size:
    x=np.random.uniform(-10,10)
    y=np.random.uniform(-10,10)
    if x**2 + y**2 <= circle_radius**2:
        set_x.append(x)
        set_y.append(y)
        dots_counter += 1


circle_angels = np.linspace(0,2*np.pi,100)
circle_x = circle_radius*np.cos(circle_angels)
circle_y = circle_radius*np.sin(circle_angels)



plt.figure(dpi=100, figsize=(6,6))
plt.title("Способ №1")
plt.plot(circle_x,circle_y,'black')
plt.plot(set_x,set_y,'.')
plt.show()

print('Mean for x\'s',np.mean(set_x))
print('Mean for y\'s',np.mean(set_y))


print('Var for x\'s',np.var(set_x))
print('Var for y\'s',np.var(set_y))

main_x = 20
main_y = 0


def distance (x1,y1,x2,y2):
    return np.sqrt((x2-x1)**2+(y2-y1)**2)

distances = []
for i in range(set_size):
    distances.append(distance(set_x[i],set_y[i],main_x,main_y))
distances.sort()

kde_distances_y = gaussian_kde(distances).evaluate(distances)

plt.figure(dpi=100)
plt.title('Плотность распределения расстояний между точками')
plt.plot(distances,kde_distances_y)
plt.hist(distances, bins=100, alpha=0.2, density= True)
plt.show()


