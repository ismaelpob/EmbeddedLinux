import struct

a=0x41be6666
a=format(a, 'x')
print(struct.unpack('!f', bytes.fromhex(a))[0])
