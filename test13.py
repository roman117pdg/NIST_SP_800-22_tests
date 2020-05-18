# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence
# mode - A switch for applying the test either forward through the input sequence (mode = 0) or
# backward through the sequence (mode = 1). 

import math
from scipy.special import gammaincc
from scipy.stats import norm


# see 2.13 section
def cumulative_sums_test(E, mode = 0):
	n = len(E)
	print(n)
	# X = []
	s = 0
	S = []
	for bit in E:
		if bit =="0":
			s -= 1
			# X.append(-1)
		else:
			s += 1
			# X.append(1)
		S.append(s)
	# print(X)
	print(S)
	z = 0
	for s in S:
		if z < abs(s):
			z = abs(s)
	print(z)
	p1 = 0
	bottom_range = int(((-n/z)+1)/4)
	upper_range = int(((n/z)-1)/4)
	for k in range(bottom_range, upper_range+1):
		p1_1 = norm.cdf(((4*k+1)*z)/math.sqrt(n))
		p1_2 = norm.cdf(((4*k-1)*z)/math.sqrt(n))
		p1 += (p1_1 - p1_2)

	p2 = 0
	bottom_range = int(((-n/z)-3)/4)
	upper_range = int(((n/z)-1)/4)
	for k in range(bottom_range, upper_range+1):
		p2_1 = norm.cdf(((4*k+3)*z)/math.sqrt(n))
		p2_2 = norm.cdf(((4*k+1)*z)/math.sqrt(n))
		p2 += (p2_1 - p2_2)

	p = 1 - p1 +p2
	return(p)
