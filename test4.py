# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# E - generated sequence

from scipy.special import gammaincc

# see 2.4 section
def test_for_the_longest_run_of_ones_in_a_block(E, M=8, K=3):
	n = len(E)
	N = int(n/M)
	v = [0, 0, 0, 0]
	pi = [0.2148, 0.3672, 0.2305, 0.1875] # see 3.4 section 
	for i in range(N):
		block = E[ i*M : (i+1)*M ]
		ones_counter = 0
		longest_counter = 0
		for j in range(M):
			if block[j] == "1":
				ones_counter += 1
				if longest_counter < ones_counter:
					longest_counter = ones_counter
			else:
				ones_counter = 0
		if longest_counter <= 1:
			v[0] += 1
		elif longest_counter == 2:
			v[1] += 1
		elif longest_counter == 3:
			v[2] += 1
		else:
			v[3] += 1
	x_obs = 0
	for i in range(K+1):
		x_obs += ((v[i]-N*pi[i])**2) / (N*pi[i])
	p = gammaincc(K/2,x_obs/2)
	return(p)
# 