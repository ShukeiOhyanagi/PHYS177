import numpy as np
import math

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

x = np.array([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5])
y = np.array([2.25,6.25,12.25,20.25,30.25,42.25,56.25,72.25,90.25,110.25])

print trap(x,y)
print simp(x,y)
