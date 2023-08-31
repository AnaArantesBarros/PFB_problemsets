import statistics
import sys
nota1 = int(sys.argv[1])
nota2 = int(sys.argv[2])
media = statistics.mean([nota1,nota2]) 
print("Sua média é de {}".format(media))
if int(media) >=5:
	print("Aprovado!")
elif int(media) <5:
	print("Reprovado!")

