import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

#swaping second and third column
data[:,[1,2]] = data[:,[2,1]]

#a)
print(f"Mjerenja su izvrsena na {len(data)} osoba")

plt.axis([0,220, 0, 180])
plt.xlabel('Height')
plt.ylabel('Weight')

#b)
plt.scatter(data[:, 2],data[:, 1])

#c)
every50Person = data[0:len(data):50]
plt.scatter(every50Person[:, 2], every50Person[:, 1])
plt.show()

#d)
height = data[:, 2]
print(height.min())
print(height.max())
print(height.mean())

#e)
ind = (data[:,0] == 1)
#zene
woman = data[ind==False, 2]
print(woman.min())
print(woman.max())
print(woman.mean())
#muskarci
men = data[ind==True, 2]
print(men.min())
print(men.max())
print(men.mean())

