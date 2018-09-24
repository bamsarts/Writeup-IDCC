import os
from pwn import *

mapping = {}
data = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}'
file = open('base','rb')
binary = file.read()
file.close()

def solve(z):
    file = open('output/' + z, 'wb')
    os.system('chmod +x output/'+z)

    file.write(binary)
    file.close()
    r = process('output/' + z)
    hasil = r.recvline()[1:-2]
    r.close()

    return hasil

def crack(z):
    first = []
    second = []
    for c in data:
        out = solve(c)
        if (out == z):
            return c
        elif (out[0] == z[0]):
            first.append(c)
    for c in data:
        for d in first:
            out = solve(d+c)
            if (out == z):
                return d+c
            elif (out[:2] == z[:2]):
                second.append(d+c)
    for c in data:
        for d in second:
            if (solve(d+c) == z):
                return d+c

flag = 'c=/2HsfweAeTCz]!V@alV@pz9??$eYjQVz&ln<z5'
decrypted = ''
for i in range(10):
    decrypted += crack(flag[i*4:i*4+4])
    file = open('flag', 'w')
    file.write(decrypted)
    file.close()