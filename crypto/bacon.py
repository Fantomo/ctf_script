#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

password_list = {
	"A": "aaaaa", "B": "aaaab", "C": "aaaba", "D": "aaabb", "E": "aabaa", "F": "aabab", "G": "aabba", "H": "aabbb", "I": "abaaa", "J": "abaab",
	"K": "ababa", "L": "ababb", "M": "abbaa", "N": "abbab", "O": "abbba", "P": "abbbb", "Q": "baaaa", "R": "baaab", "S": "baaba", "T": "baabb",
	"U": "babaa", "V": "babab", "W": "babba", "X": "babbb", "Y": "bbaaa", "Z": "bbaab"
}


def decode_bacon(bacon_str):

	pwd_list = {y:x for x, y in password_list.items()}

	flag = ''
	start = 0
	step = 5

	for i in range(len(bacon_str)/5):
		temp_str = bacon_str[start: step]
		temp_code = pwd_list[temp_str]
		start += 5
		step += 5

		flag += temp_code

	print("flag:", flag.lower())


if __name__ == '__main__':

	try:
		bacon_str = sys.argv[1]
		decode_bacon(bacon_str)

	except:
		print("Example: python bacon.py 'bacon_str'")