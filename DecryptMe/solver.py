from base64 import *

enkripsi = open('enkripsi','r').read()

integer = []

for i in range(len(enkripsi)):
	integer.append(ord(enkripsi[i]) + 127)

print integer

param = b64encode('IDCC{')
key = []

for i in range(4):
	for j in range(0,127):
		cek = integer[i] - j
		if chr(cek) == param[i]:
			key.append(j)

print key

flag = ''
for i in range(len(integer)):
	tmp = integer[i] - key[i % len(key)]
	flag += chr(tmp)

print b64decode(flag)
