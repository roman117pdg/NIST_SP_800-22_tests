# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence
# m - the length in bits of each block

from scipy.special import gammaincc

# see 2.11 section
def serial_test(E, m = 3):
	n = len(E)
	psi = [ 0 for i in range(m) ]
	for current_m in range(m,0, -1):
		# print("m = "+str(current_m))
		e = E[:] + E[:current_m-1]
		# print(e)
		v = [ 0 for i in range(2**current_m) ]
		for i in range(n):
			tmp = e[i:i+current_m]
			iterator = int(tmp,2)
			v[iterator] += 1
		# print(v)
		for frequency in v:
			psi[current_m-1] += frequency**2
		psi[current_m-1] = ((2**current_m)/n)*psi[current_m-1] - n
	# print(psi)
	delta_psi = psi[m-1] - psi[m-2]
	delta_2_psi = psi[m-1] - 2*psi[m-2] + psi[m-3]
	# print("d1 = "+str(delta_psi)+",d2 = "+str(delta_2_psi))
	p1 = gammaincc(2**(m-2),delta_psi/2)
	p2 = gammaincc(2**(m-3),delta_2_psi/2)
	return(p1, p2)
