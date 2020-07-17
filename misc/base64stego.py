#-*- encoding:utf-8 -*-

import base64

b64str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def get_Steganography(file_name):
	secret_str = ""
	with open(file_name, "r") as f:
		lines = f.readlines()

	for line in lines:
		bin_str = ""

		for code in line.strip():
			if code == "=":
				continue
			bin_str += bin(b64str.find(code)).replace("0b", "").zfill(6)

		num = len(bin_str)%8

		if num > 0:

			t_str = bin_str[-num:]
			if t_str == "0000":
				continue
			secret_str += t_str

	return secret_str


def decode_Steganography(secret_str):

	flag = ""

	for i in xrange(0, len(secret_str), 8):
		flag += chr(int(secret_str[i:i + 8], 2))

	return flag


if __name__ == '__main__':
	file_name = "./stego.txt"
	flag = decode_Steganography(get_Steganography(file_name))

	print("flag:", flag)
