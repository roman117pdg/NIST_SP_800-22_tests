# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

import math
from scipy.special import gammaincc


# see 2.12 section
def approximate_entropy_test(E, m = 2):
	n = len(E)
	print(n)
	phi = [0, 0]
	for current_m in range(m,m+2): 
		C = [ 0 for i in range(current_m) ]
		e = E[:] + E[:current_m-1]
		# print(e)
		v = [ 0 for i in range(2**current_m) ]
		c = [ 0 for i in range(2**current_m) ]
		for i in range(n):
			tmp = e[i:i+current_m]
			iterator = int(tmp,2)
			v[iterator] += 1
		# print(v)
		for i in range(len(v)):
			c[i] = v[i]/n
		# print(c)
		phi[current_m-m] = 0
		for i in range(2**current_m):
			if c[i] > 0:
				pi = c[i]
				phi[current_m-m] += pi*(math.log(pi))
	ApEnm = phi[0] - phi[1]
	print(ApEnm)
	print(math.log(2))
	x_2 = 2*n*(math.log(2) - ApEnm)
	print(x_2)
	p = gammaincc(2**(m-1),x_2/2)
	return(p)
