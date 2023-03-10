import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 3, 3, 1, 2])
y = np.array([2, 2, 1, 1, 2])


plt.plot(x,y, 'ro', color='blue')
plt.plot(x,y)
plt.axis([0, 4, 0, 4])
plt.title('Primjer')
plt.xlabel('x os')
plt.ylabel('y os')
plt.show()