import numpy as np
import math
import matplotlib.pyplot as plt

filein = 'velocities.txt'
data = np.loadtxt(filein)
t = data[:,0]
v = data[:,1]

def trap(x,y):
	N = len(x)
	integral = y[0] + y[-1]
	for k in range(1,N-2):
		integral = integral + 2*y[k]
	h = x[1] - x[0]
	return (integral*h*0.5)

def simp(x,y):
	N = len(x)
	h = x[1] - x[0]
	int1 = y[0] + y[-1]
	for k in range(1,N-2):
		if k %2 == 0:
			I1 = 2. *y[k]
			int1 = int1 + I1
		else:
			I2 = 4. *y[k] 
			int1 = int1 + I2
	Ip = 1. / 3. * h * int1
	return Ip
v_array = np.array(v)
t_array = np.array(t)

y = v_array
x = t_array

i = 0
y1 = np.zeros(len(t))
y1[0] = 0. 
while (i < len(t)-1) :
	x = t_array[0:i]
	y = v_array[0:i]
	x1 = simp(x,y)
	y1[i] = x1

ax1 = plt.subplot(2,1,1)
plt.plot(x,y)
plt.ylabel('velocity [m/s]')
ax2 = plt.subplot(2,1,2)
plt.plot(x,y1)
plt.ylabel('Distance [m]')
plt.xlabel('time  [s]')
plt.show()
