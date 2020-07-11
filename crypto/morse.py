#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

password_list = {

 	# 26 个英文字符
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

 	# 10 个数字
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

	# 16 个特殊字符
    ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
    '?': '..--..', '=': '-...-', "'": '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
    ')': '-.--.-', '$': '...-..-', '&': '. . . .', '@': '.--.-.'
}



def decode_morse(morse_str):

	pwd_list = { y:x for x,y in password_list.items()}

	flag = ''

	morse_code_list = morse_str.split(" ")

	for morse_code in morse_code_list:

		if morse_code == '':
			continue

		temp_char = pwd_list[morse_code]
		flag += temp_char

	print("flag:", flag.lower())


def encode_mores(src_str):

	morse_str = ''

	for t_char in src_str.upper():
		morse_code = password_list[t_char]
		morse_str += morse_code + " "

	morse_str = morse_str.strip()

	print ("morse_str:", morse_str)



if __name__ == '__main__':


	try:
		command = sys.argv[1]
		input_string = sys.argv[2]
		if command.upper() == 'ENCODE':
			encode_mores(input_string)
		elif command.upper() == 'DECODE':
			decode_morse(input_string)
		else:
			raise

	except:
		print("Example: python morse.py [encode|decode] 'str'")
