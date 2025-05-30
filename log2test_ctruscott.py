# Charles Truscott

"""

0b1
0b10
0b100
0b1000
0b10000
0b100000
0b1000000
0b10000000
0b100000000
0b1000000000
0b10000000000
0b100000000000
0b1000000000000
0b10000000000000
0b100000000000000
0b1000000000000000
0b10000000000000000
0b100000000000000000
0b1000000000000000000
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
Modulo n to the x, 1
Caught it
Modulo n to the x, 2
Caught it
Modulo n to the x, 3
Caught it
Modulo n to the x, 4
Caught it
Modulo n to the x, 5
Caught it
Modulo n to the x, 6
Caught it
Modulo n to the x, 7
Caught it
Modulo n to the x, 8
Caught it
Modulo n to the x, 9
Caught it
Modulo n to the x, 10
Caught it
Modulo n to the x, 11
Caught it
Modulo n to the x, 12
Caught it
Modulo n to the x, 13
Caught it
Modulo n to the x, 14
Caught it
Modulo n to the x, 15
Caught it
Modulo n to the x, 16
Caught it
Modulo n to the x, 17
Modulo n to the x, 18
Modulo n to the x, 1
Caught it
Modulo n to the x, 2
Caught it
Modulo n to the x, 3
Caught it
Modulo n to the x, 4
Caught it
Modulo n to the x, 5
Caught it
Modulo n to the x, 6
Caught it
Modulo n to the x, 7
Caught it
Modulo n to the x, 8
Caught it
Modulo n to the x, 9
Caught it
Modulo n to the x, 10
Caught it
Modulo n to the x, 11
Caught it
Modulo n to the x, 12
Caught it
Modulo n to the x, 13
Caught it
Modulo n to the x, 14
Caught it
Modulo n to the x, 15
Caught it
Modulo n to the x, 16
Caught it
Modulo n to the x, 17
Modulo n to the x, 18
Modulo n to the x, 1
Caught it
Modulo n to the x, 2
Caught it
Modulo n to the x, 3
Caught it
Modulo n to the x, 4
Caught it
Modulo n to the x, 5
Caught it
Modulo n to the x, 6
Caught it
Modulo n to the x, 7
Caught it
Modulo n to the x, 8
Caught it
Modulo n to the x, 9
Caught it
Modulo n to the x, 10
Caught it
Modulo n to the x, 11
Caught it
Modulo n to the x, 12
Caught it
Modulo n to the x, 13
Caught it
Modulo n to the x, 14
Caught it
Modulo n to the x, 15
Caught it
Modulo n to the x, 16
Caught it
Modulo n to the x, 17
Modulo n to the x, 18
Modulo n to the x, 1
Caught it
Modulo n to the x, 2
Caught it
Modulo n to the x, 3
Caught it
Modulo n to the x, 4
Caught it
Modulo n to the x, 5
Caught it
Modulo n to the x, 6
Caught it
Modulo n to the x, 7
Caught it
Modulo n to the x, 8
Caught it
Modulo n to the x, 9
Caught it
Modulo n to the x, 10
Caught it
Modulo n to the x, 11
Caught it
Modulo n to the x, 12
Caught it
Modulo n to the x, 13
Caught it
Modulo n to the x, 14
Caught it
Modulo n to the x, 15
Caught it
Modulo n to the x, 16
Caught it
Modulo n to the x, 17
Modulo n to the x, 18
[[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]]
0b1
0b10
0b100
0b1000
0b10000
0b100000
0b1000000
0b10000000
0b100000000
0b1000000000
0b10000000000
0b100000000000
0b1000000000000
0b10000000000000
0b100000000000000
0b1000000000000000
0b10000000000000000

[Program finished]

"""
from queue import deque
def Power():
	n = 2
	for x in range(0, 18 + 1):
		print(bin(n ** x))
		yield n ** x
		
def count():
	c = 1
	max = 2 ** 17
	while c < max:
		yield c
		c  <<= 1
		
def Choose(bs):
	if (bs % 2 ** 18) == 0:
		print("Modulo n to the x, 18")
		pass
	elif (bs % 2 ** 17) == 0:
		print("Modulo n to the x, 17")
		pass
	elif (bs % 2 ** 16) == 0:
		print("Modulo n to the x, 16")
		print("Caught it")
		pass
	elif (bs % 2 ** 15) == 0:
		print("Modulo n to the x, 15")
		print("Caught it")
		pass
	elif (bs % 2 ** 14) == 0:
		print("Modulo n to the x, 14")
		print("Caught it")
		pass
	elif (bs % 2 ** 13) == 0:
		print("Modulo n to the x, 13")
		print("Caught it")
		pass
	elif (bs % 2 ** 12) == 0:
		print("Modulo n to the x, 12")
		print("Caught it")
		pass
	elif (bs % 2 ** 11) == 0:
		print("Modulo n to the x, 11")
		print("Caught it")
		pass
	elif (bs % 2 ** 10) == 0:
		print("Modulo n to the x, 10")
		print("Caught it")
		pass
	elif (bs % 2 ** 9) == 0:
		print("Modulo n to the x, 9")
		print("Caught it")
		pass
	elif (bs % 2 ** 8) == 0:
		print("Modulo n to the x, 8")
		print("Caught it")
		pass
	elif (bs % 2 ** 7) == 0:
		print("Modulo n to the x, 7")
		print("Caught it")
		pass
	elif (bs % 2 ** 6) == 0:
		print("Modulo n to the x, 6")
		print("Caught it")
		pass
	elif (bs % 2 ** 5) == 0:
		print("Modulo n to the x, 5")
		print("Caught it")
		pass
	elif (bs % 2 ** 4) == 0:
		print("Modulo n to the x, 4")
		print("Caught it")
		pass
	elif (bs % 2 ** 3) == 0:
		print("Modulo n to the x, 3")
		print("Caught it")
		pass
	elif (bs % 2 ** 2) == 0:
		print("Modulo n to the x, 2")
		print("Caught it")
		pass
	elif (bs % 2 ** 1) == 0:
		print("Modulo n to the x, 1")
		print("Caught it")
		pass
	elif (bs == 0):
		print("1")
		pass
	return bs
L = []
for e in Power():
	L.append(e)
print(L)
all_L = []
for bs in L:
	Choose(bs)
for n in range(0, 3):
	all_L.append(list(Choose(bs) for bs in L))
print(all_L)
for n in count():
	print(bin(n))
#Solution below is in polynomial time. I'm hoping to implement an optimal, logarithmic algorithm'
#c1 = 0
#c2 = 0
#c3 = c1 + 1
#while c1 < len(all_L):
#	while c2 < len(all_L[0]):
#		print("inner")
#		print(c2)
#		c2 += 1	
#	print("outer")
#	print(c1)
#	c2 = 0
#	c1 += 1