import numpy as np
import math

h = 800.00

i = input('Type in a initial velocity in m/s: ')
v = float(i)

vf = math.sqrt(v*v + 2*h*9.81)
t = (vf - v)/9.81

print "Ball takes",(t),"seconds to reach the ground."
