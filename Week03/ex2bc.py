import numpy as np
from numpy.linalg import solve
import pdb

V = np.array([[4,-1,-1,-1],[-1,3,0,-1],[-1,0,3,-1],[-1,-1,-1,4]],float)
v = np.array([5,0,5,0],float)

N = len(v)

for m in range(N):
	a = V[m,m]
	V[m,:] /= a
	v[m] /= a
	for i in range(m+1, N):
		b = V[i,m]
		V[i,:] -= b*V[m,:]
		v[i] -= v[m]*b

x = np.array([0.,0.,0.,0.],float)
for n in range(N-1,-1,-1):
	x[n] = v[n]
	for j in range(n+1, N):
		x[n] -= V[n,j]*x[j]

x2 = solve(V,v)
print "Result by own Gaussian elimination:",x
print "Result by intrinsic function:",x2
