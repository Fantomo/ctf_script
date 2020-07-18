#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

decode_str = "abcdefghijklmnopqrstuvwxyz"


def decode_caesar(ciphertext):
    flag = ''
    
    for tmp_char in ciphertext:
        if tmp_char in ['{', '_', '}']:
            flag += tmp_char
        else:
            decode_index = decode_str.index(tmp_char)
            index = decode_index + offset
            if index > 25:
                index -= 26
            tmp_char = decode_str[index]
            flag += tmp_char

    print("flag:", flag)


if __name__ == '__main__':
    try:
        ciphertext = sys.argv[1]
        offset = int(sys.argv[2])
        if offset <= 25:
        	decode_caesar(ciphertext.lower())
        else:
        	print ("Error: offset must be Less than 26")
    except:
        print ("Example: python caesar.py ciphertext offset")
