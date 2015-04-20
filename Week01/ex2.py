import numpy as np
import math
import sys
import matplotlib.pyplot as plt

H = np.array([10, 10, 8, 9.5, 3, 9, 0, 6])
M = np.array([10, 10, 10, 10, 8, 5, 10, 7])
F = np.array([9, 10, 10, 6, 10, 6, 8, 9])

G = 0.4 * H + 0.2 * M + 0.4 * F
log = open('grade.txt','a')
print >> log, G[:, np.newaxis]
log.close()


O1 = 0
F1 = 0

O2 = O1

for i in range(len(G)):
	if G[i] < 6:
		F1 = F1 + 1 
		print "Number of failed student: ", (F1)
		print "Their grade: ", G[i]
	if G[i] > 9.5:
		O1 = O1 + 1
		list = [O1]

print "Fraction of outstanding student:",(O1), "/8"

plt.hist(G)
plt.xlabel("Grades")
plt.ylabel("N")
plt.savefig('classgrade.png',format='PNG')
plt.show()
