
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

circle_radius = 10
set_size = 1000

set_x = []
set_y = []
dots_counter = 0
while dots_counter < set_size:
    h=np.random.uniform(0,10)
    circle_angels_h = np.random.uniform(0,2*np.pi)
    set_x.append(h*np.cos(circle_angels_h))
    set_y.append(h*np.sin(circle_angels_h))
    dots_counter += 1




circle_angels = np.linspace(0,2*np.pi,100)
circle_x = circle_radius*np.cos(circle_angels)
circle_y = circle_radius*np.sin(circle_angels)



plt.figure(dpi=100, figsize=(6,6))
plt.title("Способ №2")
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



