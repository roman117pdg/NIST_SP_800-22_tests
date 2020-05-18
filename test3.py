# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

import math

# see 2.3 section
def runs_test(E):
	n = len(E)
	pi = 0
	for bit in E:
		pi += int(bit)
	pi /= n
	tau = 2/math.sqrt(2)
	if abs(pi - 0.5) >= tau:
		p = 0
		return p
	else:
		V_n_obs = 1
		for i in range(n-1):
			if E[i] != E[i+1]:
				V_n_obs += 1
		p = math.erfc( abs(V_n_obs - 2*n*pi*(1-pi)) / (2*math.sqrt(2*n)*pi*(1-pi)) )
		return p