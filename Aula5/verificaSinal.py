import sys
valor= int(sys.argv[1])
if valor < 0:
	print("Seu número é negativo")
elif valor > 0:
	print("Seu número é positivo")
	if valor < 50:
		print("É menor que 50")
		if valor%2 == 0: #Input verifica o resto da divisão
			print("É número par!")
	elif valor > 50:
		print("É maior que 50")
else:

	print("Seu número é zero.")
