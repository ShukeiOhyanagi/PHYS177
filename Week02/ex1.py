import numpy as np
import math

def TrapeRule(f,a,b,N):	
	h = (b-a) / float(N)
	I = f(a) + f(b)
	for k in range(1,N):
		I = I + 2*f(a + k*h)

	Ip = 0.5*I*h
	return Ip

def SimpRule(f,h):
	a = np.array(h)
	b = np.array(-h)
	I = 1. / 3. * h * (f(b)+4*f(0)+f(a))
	return I

def f(x):
	return 2*x**2 + 3*x + 4


a = -5.
b = 5.
N = 10
h = 5.0

print TrapeRule(f,a,b,N)
print SimpRule(f,h)
