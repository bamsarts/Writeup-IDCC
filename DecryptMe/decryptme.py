from base64 import *

def enkripsi(plain, text)
	enc = []
	plain = b64encode(plain)
	for i, l in enumerate(plain):
		kunci = ord(keys[i % len(keys)])
		teks = ord(l)
		enc.append(chr((teks + kunci) % 127))
	return ''.join(enc)


