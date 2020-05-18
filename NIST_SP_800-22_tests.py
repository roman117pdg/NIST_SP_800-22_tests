from test1 import frequency_test
from test2 import frequency_test_within_a_block
from test3 import runs_test
from test4 import test_for_the_longest_run_of_ones_in_a_block
from test5 import binary_matrix_rank_test
from test6 import discrete_fourier_transform_test
from test7 import non_overlapping_template_matching_test
from test8 import overlapping_template_matching_test
from test9 import maurers_universal_statistical_test
from test10 import linear_complexity_test
from test11 import serial_test
from test12 import approximate_entropy_test
from test13 import cumulative_sums_test
from test14 import random_excursions_test
from test15 import random_excursions_variant_test
# import tmp

# # import euler form file
# import pickle
# input_file = open("euler_num.bin", "rb")
# E = pickle.load(input_file)


# # test 1, expected p = 0.109599 [OK]
# E = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
# print(frequency_test(E))

# test 2, expected p = 0.706438 [OK]
# E = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
# print(frequency_test_within_a_block(E, M=10))

# # test 3, expected p = 0.500798 [OK]
# E = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
# print(runs_test(E))

# # test 4, expected p = 0.180609 [OK]
# E = "11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010"
# print(test_for_the_longest_run_of_ones_in_a_block(E))

# # test 5, expected p = 0.741948 [OK]
# E = "01011001001010101101"
# print(binary_matrix_rank_test(E, 3, 3))

# # test 6, expected p = 0.029523 [OK]
# E = "1001010011"
# print(discrete_fourier_transform_test(E))

# # test 7, expected p = 0.344154 [OK]
# E = "10100100101110010110"
# print(non_overlapping_template_matching_test(E,3,2))

# # test 8, expected p = 0.274932 [NOT OK] but i found error in this example descrption (in step2 second block have wrong v[])
# E = "10111011110001110100011100101110111110000101101001"
# print(overlapping_template_matching_test(E, m = 2, N = 5, K = 2, M = 10))

# # test 9, expected p = 0.767189 [OK]
# E = "01011010011101010111"
# print(maurers_universal_statistical_test(E, L=2, Q=4))

# # test 10, they don't give example to this one
# E = "1101011110001"
# E = "11010111100011101011110001110101111000111010111100011101011110001"
# print(linear_complexity_test(E, 13))
# print("--------------------------------------------------------------")
# print(tmp.maurers_universal_test(E))

# # test 11, expected p1 = 0.9057, p2 = 0.8805 [dunno ]
# E = "0011011101"
# [p1, p2] = serial_test(E, 3)
# print("p1 = "+str(p1)+",p2 = "+str(p2))

# # test 12, expected p = 0.261961 [OK] but i found errors in example ;P
# E = "0100110101"
# print(approximate_entropy_test(E,3))

# # test 13, expected p = 0.4116588 [OK]
# E = "1011010111"
# print(cumulative_sums_test(E))

# # test 14, expected p = 0.502529 (5-th value) [OK]
# E = "0110110101"
# print(random_excursions_test(E)[4])

# # test 15, expected p = 0.683091 (9-th value)  [OK]
# E = "0110110101"
# print(random_excursions_variant_test(E)[9])
