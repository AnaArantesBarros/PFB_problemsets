import sys
ano =int(sys.argv[1])
if ano%4 == 0:
	if ano%100 != 0:
		print("É ano bissexto!")
	else:
		print("Não é bissexto!")
else:
	print("Não é bissexto")
