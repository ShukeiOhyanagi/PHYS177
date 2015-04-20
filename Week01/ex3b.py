import numpy as np
import math
import matplotlib.pyplot as plt

h = 800.00

i = input('Type in a minimum velocity in m/s: ')
vmin = float(i)
f = input('Type in a maximum velocity in m/s: ')
vmax = float(f)

b = (vmax - vmin)/9
vn = vmin
n = 0
t1 = []
vi = []

while(vn < vmax):
	vn = vmin + b*n
	vf = math.sqrt(vn*vn + 2*h*9.81)
	t = (vf - vn)/9.81
	n += 1
	t1.append(t)
	vi.append(vn)

t1_array = np.array(t1)
vi_array = np.array(vi)
np.savetxt('fallingtime.txt',t1_array)

x = vi_array
y = t1_array
plt.plot(x,y)
plt.xlabel("v_init (m/s)")
plt.ylabel("t (second)")
plt.savefig('time_vs_vi.png',format='PNG')
plt.show()
