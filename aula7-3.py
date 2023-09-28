"""numero = 0
while numero < 100:
	numero += 1 
	print(numero)
numero = 0
resultado = 1
while numero < 5:
	numero += 1
	resultado = resultado * numero
print(resultado)"""

loop = [101,2,15,22,95,33,2,27,72,15,52]
for i in loop:
	if i%2 == 0:
		print(str(i) +  " é par!")
	else:
		pass
par = 0
impar = 0
for n in loop:
	#print(n)
	if n%2 == 0:
		impar += n
	elif n%2 != 0:
		par += n
print(impar,par)
