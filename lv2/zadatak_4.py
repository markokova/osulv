import numpy as np
import matplotlib.pyplot as plt


whiteSquare = np.zeros((50,50))
blackSquare = np.ones((50,50))

blackWhiteColumn = np.vstack((whiteSquare,blackSquare))
whiteBlackColumn = np.vstack((blackSquare,whiteSquare))
wholePicture = np.hstack((blackWhiteColumn, whiteBlackColumn))

plt.imshow(wholePicture, cmap='gray')

plt.axis([0,100,100,0])
plt.show()