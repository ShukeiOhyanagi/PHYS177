
import numpy as np
import math

def TrapeRule(f,a,b,N):	
	h = (b-a) / float(N)
	I = f(a) + f(b)
	for k in range(1,N):
		I = I + 2*f(a + k*h)

	Ip = 0.5*I*h
	return Ip

def SimpRule(f,a,b,N):
	h = (b-a) / float(N)
	I = f(a) + f(b)
	for k in range(1,N):
		if k %2 == 0:
			I1 = 2*f(a + k*h)
			I = I + I1
		else:
			I2 = 4*f(a + k*h) 
			I = I + I2
	Ip = 1. / 3. * h * I
	return Ip

def f(x):
	return 2*x**2 + 3*x + 4 


a = 0.
b = 5.
N = 10

print TrapeRule(f,a,b,N)
print SimpRule(f,a,b,N)

