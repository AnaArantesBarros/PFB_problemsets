import sys
import re
file = sys.argv[1]
with open ("Python_08.fasta") as fasta:
	for linha in fasta:
		linha = linha.rstrip()
		if linha.startwith(">"):
			linhas_juntas = ""
			geneID = re.search(r"^>([\w]{8,10}",linha).group(1)
		else:
			linhas_juntas += linha.strip()
		codons = re.findall(r".{3}"), linhas_juntas.replace("\n",""))
		sequencia[geneId] = "".join(linhas_juntas)

with open("Python_08.fasta") as fasta:
	for geneID in sequencia.keys():
		codons = re.findall(r".{3}", sequencia[geneID])
		headline = 
		
