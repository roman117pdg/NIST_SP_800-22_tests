# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

import math

# see 2.15 section
def random_excursions_variant_test(E):
	n = len(E)
	# print(n)
	s = 0
	S = []
	S.append(0)
	J = 0
	for bit in E:
		if bit =="0":
			s -= 1
		else:
			s += 1
		S.append(s)
		if s == 0:
			J += 1
	S.append(0)
	J += 1
	# print(S)
	# print(J)
	ksi = [ 0 for i in range(18) ]
	for value in S:
		if value > 0 and value <= 9:
			ksi[value+8] += 1
		elif value < 0 and value >= -9:
			ksi[value+9] += 1
	# print(ksi)

	p = [ 0 for i in range(18) ]
	for i in range(18):
		x = 0
		if i >= 0 and i < 9:
			x = 9-i
		elif i >= 9 and i < 19:
			x = i-8
		# print("i:"+str(i)+", x:"+str(x))
		p[i] = math.erfc(abs(ksi[i]-J)/math.sqrt(2*J*(4*x-2)))
	return(p)
