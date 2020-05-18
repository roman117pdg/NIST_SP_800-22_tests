# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence
# L - the length of each block
# Q	- the number of blocks in the initialization sequence
# K	- the number of blocks in the test sequence

# n = 20, L = 2, Q = 4, K = 6

import math

# see 2.9 section
def maurers_universal_statistical_test(E, L = 8, Q = 2560):
	n = len(E)
	K = int((n/L) - Q)
	# print(K)
	blocks = [E[L*i:L*(i+1)] for i in range(Q+K)]
	T = [ 0 for i in range(2**L)]
	for i in range(Q):
		T[int(blocks[i],2)] = i+1
	# print(T)
	sum = 0
	for i in range(Q,Q+K):
		j = int(blocks[i],2)
		sum += math.log((i+1 - T[j]),2)
		T[j] = i+1
	# print(sum)
	# print(T)
	fn = sum/K
	# print(fn)
	# tables for L = <1,16>
	expectedValue = [0,0.73264948,1.5374383,2.40160681,3.31122472,4.25342659,5.2177052,6.1962507,7.1836656,8.1764248,9.1723243,10.170032,11.168765,12.168070,13.167693,14.167488,15.167379]
	variance = [0,0.690,1.338,1.901,2.358,2.705,2.954,3.125,3.238,3.311,3.356,3.384,3.401,3.410,3.416,3.419,3.421]
	p = math.erfc(abs((fn - 1.5374383)/(math.sqrt(2)*math.sqrt(variance[L]))))
	return(p)
