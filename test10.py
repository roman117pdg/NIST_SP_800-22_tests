# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence
# M - the length in bits of a block
# K - the number of degrees of freedom (eq = 6)

from scipy.special import gammaincc

# see 2.10 section
def linear_complexity_test(E, M=1000):
	n = len(E)
	K = 6
	N = int(n/M)
	blocks = [E[i*M:(i+1)*M] for i in range(N)]
	u = (M/2) + ((9 + (-1)**(M+1))/36) - ((M/3 +2/9)/(2**M))
	# print(u)

	# Berlekamp-Massey algorithm + calculating T values
	# based on https://stackoverflow.com/questions/50517576/berlekamp-massey-minimal-lfsr-issues and https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm
	L_table = []
	T_table = []
	for block in blocks:
			n = len(block)
			S = [int(bit) for bit in block]
			B = [ 0 for i in range(n)]
			C = [ 0 for i in range(n)]
			B[0] = 1
			C[0] = 1
			L = 0
			m = -1
			for N in range(n):
				d = S[N]
				for j in range(1, L+1):
					d ^= (C[j] & S[N-j])
				if d != 0:
					T = C[:]
					for j in range(0, n-N+m):
						C[N-m+j] ^= B[j]
					if 2*L <= N:
						L = N+1-L
						m = N
						B = T[:]
			L_table.append(L)
			T = ((-1)**M)  * (L-u) + (2/9)
			T_table.append(T)
	# print(L)
	# print(T_table)
	# ! Berlekamp-Massey algorithm
	v = [ 0 for i in range(K+1)]
	# print(v)
	for T in T_table:
		if T <= -2.5:	v[0] += 1
		elif T <= -1.5:	v[1] += 1
		elif T <= -0.5:	v[2] += 1
		elif T <=  0.5:	v[3] += 1
		elif T <=  1.5:	v[4] += 1
		elif T <=  2.5:	v[5] += 1
		elif T > 2.5:	v[6] += 1

	pi = [ 0.010417, 0.03125, 0.125, 0.5, 0.25, 0.0625, 0.020833 ]
	X_2_obs = 0
	for i in range(K+1):
		X_2_obs += ((v[i] - N*pi[i])**2)/N*pi[i]
	# print(X_2_obs)
	p = gammaincc(K/2, X_2_obs/2)
	return(p)
