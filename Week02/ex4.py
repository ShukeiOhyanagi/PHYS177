import numpy as np
import math


def trap(x,y):
	N = len(x) 
	h = x[1] - x[0]
	I = 0.
	for k in range(0,N):
		if k %2. != 0.:
			I = I + y[k]
	return (I*h)
fx = []
fy = []
fx1 = []
fy1 = []
fx2 = []
fy2 =[]
x = 1.
x1 = 0.
x2 = 0.
y = 0.
y1 = 0.
y2 = 0.
n = 1

for i in range(0,n+1):
	x = i
	fx.append(x)
	y = (math.sin(10.*math.sqrt(x)))**2
	fy.append(y)
T = trap(x=fx, y=fy)
print "Number of slice: ",n
print "Estimate value of integration: ",T
print "Error on estimated value: NA"

n = n*2
for k in range(0,n+1):
	x1 = 1./(n) * k 
	fx1.append(x1)
	y1 = (math.sin(10.*math.sqrt(x1)))**2
	fy1.append(y1)
T1 = 0.5*T + trap(x=fx1, y=fy1)
eT = 1. / 3. *(T1 - T)
print "Number of slices: ",n
print "Estimate value of integration: ",T1
print "Errror on estimated value.: ",eT

while (math.fabs(eT) > 0.000001):
	T = T1
	n = n * 2
	for j in range(0,n+1):
		x2 = 1./n * j 
		fx2.append(x2)
		y2 = (math.sin(10.*math.sqrt(x2)))**2
		fy2.append(y2)
	T1 = 0.5*T + trap(x=fx2, y=fy2)
	print "Number of slices: ",n
	print "Estimate value of integration: ",T1
	eT = 1. / 3. * (T1 - T)
	print "Error of estimated value: ",math.fabs(eT)
	del fx2[0:n+1]
	del fy2[0:n+1]



