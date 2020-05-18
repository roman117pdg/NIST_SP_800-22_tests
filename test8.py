# based on https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
# n - the length of the bit string
# m - the length in bits of each template
# E - generated sequence
# B - the m-bit template to be matched
# M - the length in bits of the substring of ε to be tested.
# N - the number of independent blocks. N has been fixed at 8 in the test code

import random
from scipy.special import gammaincc


# see 2.8 section
def overlapping_template_matching_test(E, m = 10, N = 968, K = 5, M = 1032):
	n = len(E)
	# print(n)
	blocks = [ E[i*M:(i+1)*M] for i in range(N) ]
	print(blocks)
	B = ""
	for i in range(m):
		B += "1"
	v = [ 0,0,0,0,0,0 ] 
	for i in range(len(blocks)):
		count = 0
		for position in range(M-m+1):
			# print(" > block:"+str(i)+" position:"+str(position))
			if blocks[i][position:position+m] == B:
				count += 1
			# 	print("HIT "+str(B)+" == "+str(blocks[i][position:position+m]))
			# else:
			# 	print("    "+str(B)+" != "+str(blocks[i][position:position+m]))
		if count > 5:
			v[5] += 1
		else:
			v[count] += 1
	# print(v)
	lambda_ = (M-m+1) / (2**m)
	eta = lambda_/2
	# print(lambda_)
	# print(eta)
	pi = [0.324652,0.182617,0.142670,0.106645,0.077147,0.166269] # example
	# pi = [0.364091, 0.185659, 0.139381, 0.100571, 0.070432, 0.139865] # normal
	X_2_obs = 0
	for i in range(6):
		X_2_obs += ((v[i]- N*pi[i])**2) / (N*pi[i])
	# print(X_2_obs)
	p = gammaincc(5/2, X_2_obs/2)
	return(p)


