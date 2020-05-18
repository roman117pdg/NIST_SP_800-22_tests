# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

from scipy.special import gammaincc

# see 2.2 section
def frequency_test_within_a_block(E, M=8):
	n = len(E)
	N = int(n/M)
	pi = []
	for i in range(N):
		pi.append(0)
		for j in range(M):
			pi[i] += int(E[(i*M)+j])
		pi[i] /= M
	X = 0
	for i in range(N):
		X += (pi[i] - 0.5)**2
	X *= 4*M
	p = gammaincc(N/2,X/2)
	return p
