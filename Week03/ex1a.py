import numpy as np
import math
import matplotlib.pyplot as plt

k = 1. / (4. * math.pi * 0.0008854187817)
q1 = 1.
q2 = -1.
phi = np.zeros([101,101])
def r1(x,y):
	r1 =  math.sqrt((x-55.)**2.+(y-50.)**2)
	k = 1. / (4. * math.pi * 0.0008854187817)
	q1 = 1.
	if r1 == 0.:
		return 0.
	else:
		return k*q1 / r1
def r2(x,y): 
	r2 =  math.sqrt((x-45.)**2 + (y-50.)**2.)
	k = 1. / (4. * math.pi * 0.0008854187817)
	q2 = -1.
	if r2 == 0.:
		return 0.
	else:
		return k*q2 / r2


for i in range(100):
	x = float(i)
	for j in range(100):
		y = float(j)
		phi[j,i] = r1(x,y) + r2(x,y)    
                  

plt.imshow(phi, origin='lower')
#plt.pcolormesh(x,y,phi)
plt.colorbar()
plt.show()
