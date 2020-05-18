# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

import math

# see 2.1 section
def frequency_test(E):
	n = len(E)
	S_n = 0
	for bit in E:
		if bit == "0":
			S_n -= 1
		else:
			S_n += 1 
	S_obs = abs(S_n)/math.sqrt(n)
	p = math.erfc(S_obs/math.sqrt(2))
	return p