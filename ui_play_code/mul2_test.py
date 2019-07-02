import random
import numpy as np
import matplotlib.pyplot as plt

def graph_stuff(subplot_num, max_rand):
    plt.subplot(subplot_num)
    for i in range(10):
        
        y = np.random.random()
        plt.plot(1,i, y)
        plt.pause(0.05)


plt.figure(1)                # the first figure
plt.subplot(221)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(222)             # the second subplot in the first figure
plt.plot([1, 1, 1])
plt.subplot(223)
plt.plot([2, 2, 2])

graph_stuff(224, 5)

plt.show()
