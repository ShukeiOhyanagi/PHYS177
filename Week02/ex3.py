import numpy as np
import math
from scipy.integrate import simps
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

fx = []
fy = []

x = 0.
y = 0.
n = 20
for i in range(1,n+1):
	x = 2./n * i 
	fx.append(x)
	y = x**4. - 2.*x + 1.
	fy.append(y)

print "Trapezoidal'rule by own: ",trap(x=fx, y=fy)
print "Simpson's rule by own: ",simp(x=fx, y=fy)

fx2 = np.trapz(y=fy, x=fx)
def f(x):
	return simps(fy, fx)
print "Intrinsic trapezoidal rule: ", fx2
print "Intrinsic Simpson's rule: ", f(x)

fx3 = []
fy3 = []
x3 = 0.
y3 = 0.
n = 10
for k in range(1,n+1):
	x = 2./n * k 
	fx3.append(x3)
	y = x**4. - 2.*x + 1.
	fy3.append(y3)

T = trap(x=fx3, y=fy3)
S = simp(x=fx3, y=fy3)

true = 4.4
eT = 1. / 3. * (true - T)
eS = 1. /15. * (true - S)

print "Error in trapezoidal rule with N=10: ", eT
print "Error in Simpson's rule with N=10: ", eS
