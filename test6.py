# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

import math
from numpy.fft import fft

# see 2.6 section
def discrete_fourier_transform_test(E):
	n = len(E)
	X = []
	for bit in E:
		if bit == "1":
			X.append(1)
		else:
			X.append(-1)
	S = fft(X)
	M = abs(S[:int(n/2)])
	T = math.sqrt(math.log(1/0.05)*n)
	N_0 = 0.95*n/2
	N_1 = 0
	for peak in M:
		if peak < T:
			N_1 += 1
	d = (N_1 - N_0) / math.sqrt(n*0.95*0.05/4)
	p = math.erfc(2.176429/math.sqrt(2))
	return p