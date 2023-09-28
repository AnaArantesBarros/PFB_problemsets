import sys
inicio = int(sys.argv[1])
fim = int(sys.argv[2])

for n in range(inicio,fim):
	if n%2 != 0:
		print(n)
