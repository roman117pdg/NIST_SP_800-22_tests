# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

from scipy.special import gammaincc


# see 2.14 section
def random_excursions_test(E):
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
	x = [ [ 0 for i in range(8) ] for j in range(J)]
	cycle = -1
	for s in S:
		if s == 0:
			cycle +=1
		elif s > 0 and s <= 4:
			x[cycle][s+3] += 1
		elif s < 0 and s >= -4:
			x[cycle][s+4] += 1
	# print(x)
	v = [ [ 0 for i in range(8) ] for j in range(6)]
	for i in range(8):
		for j in range(J):
			iterator = x[j][i]
			if iterator >= 0 and iterator <= 5:
				v[iterator][i] += 1
	# print(v)
	
	pikx = [[0.5, 0.25, 0.125, 0.0625, 0.0312, 0.0312],
			[0.75, 0.0625, 0.0469, 0.0352, 0.0264, 0.0791],
			[0.8333, 0.0278, 0.0231, 0.0193, 0.0161, 0.0804],
			[0.875, 0.0156, 0.0137, 0.012, 0.0105, 0.0733]]

	p = [ 0 for i in range(8) ]
	for i in range(8):
		X_2_obs = 0
		for k in range(6):
			t = ((v[k][i] - J*pikx[i%4][k])**2)
			b = (J*pikx[i%4][k])
			X_2_obs += (t / b)
		# print(X_2_obs)
		p[i] = gammaincc(5/2, X_2_obs/2)
	return(p)
