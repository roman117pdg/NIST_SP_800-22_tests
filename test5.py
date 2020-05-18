# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

import math
from numpy.linalg import matrix_rank

# see 2.5 section
def binary_matrix_rank_test(E, M=32, Q=32):
	n = len(E)
	E = [ int(bit) for bit in E ]
	N = int(n/(M*Q))
	# get rank of matrixes
	rank = []
	for j in range(N):
		matrix = [E[(j*Q + i)*M : (j*Q + i+1)*M] for i in range(Q) ]
		rank.append(matrix_rank(matrix))
	F_M = 0
	F_M_1 = 0
	for i in range(N):
		if rank[i] == M:
			F_M += 1
		elif rank[i] == M-1:
			F_M_1 += 1
	X_2_obs = 0
	X_2_obs += ((F_M-0.2888*N)**2)/(0.2888*N)
	X_2_obs += ((F_M_1-0.5776*N)**2)/(0.5776*N)
	X_2_obs += ((N-F_M-F_M_1-0.1336*N)**2)/(0.1336*N)
	p = math.e**(-X_2_obs/2)
	return p