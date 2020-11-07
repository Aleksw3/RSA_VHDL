import random

file = open('stimulus','w')

def b(a, bits):
	a = str(bin(a))[2:]
	for i in range(bits-len(a)):
		a="0"+a
	return a

def monpro(a,b,n):
	u = 0 
	# print(a,b,n)
	for bit in a[::1]:
		# print(bit)
		if bit=='1':
			u+=b
		if u%2 != 0:
			u+=n
		u//=2
	# print(u)
	return u

#Check whether RM%N = (R^2)M(r^-1)%N

upperLim = 8

# file.write("# Column Description:\n# ID | X | Y | N | Z\n")

R = 2**upperLim
A = b(R**2, upperLim)

for i in range(1):
	N = random.randint(10, 2**(upperLim-1))
	# A = random.randint(3, 2*N - 1)
	B = random.randint(3, 2*N - 1)
	# A = b(A, upperLim)
	u = monpro(A,B,N)
	print(f"Value of A:\t{R}\nValue of B:\t{B}\nValue of N:\t{N}")
	print(f"Value of RM%N: {(R*B)%N}\tValue of MonPro: {u}")
	# if(R*B)%N==u:
	# 	print(f"Value of RM%N: {(R*B)%N}\tValue of MonPro: {u}")
	# else:
	# 	print("Fuck my life")

# 	file.write(f"{i} {A} {b(B,upperLim)} {b(N,upperLim)} {b(int(u),upperLim)}\n")