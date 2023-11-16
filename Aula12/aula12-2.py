import re
import sys
sequencia = {}
codons_frames = {}


translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}


with open ("Python_08.fasta") as fasta:
	for linha in fasta:
	linha = linha.rstrip().upper()
		if linha.startwith(">"):
			linhas_juntas = ""
			geneID = re.search(r"^>([\w]{8,10})",linha).group(1)
		else:
			linhas_juntas += linha.strip()
		sequencia[geneID] = "".join(linhas_juntas)

	for geneID in sequencia.keys()
		reverseSeq = sequencia[geneID][: :-1]
		reverseSeq.replace("A", "t")
		reverseSeq.replace("T", "a")
		reverseSeq.repalce("C", "g")
		reverseSeq.replace("G", "c")
		reserseSeq = reverseSeq.upper()
		codons_frames[geneID] = {}
	
		for frame in range(3):
			codons = re.findall(r".{3}", sequencia[geneID][frame:])
			frameID = "frame_+" + str(frame+1)
			codons_frames[geneID][frameID] = codons
			codonsReverse = re.findall(r".{3}", reverseSeq[frame:])
			frameID_reverse = "frame_-" + str(frame+1)
			codons_frames[geneID][frameID_reverse] = codonsReverse
	#For para tradução
	for geneID in codons_frames.keys():
		protein_frames = ""
		protein = ""
		for frame in codons_frames[geneID]:
			protein = ""
			for codon in codons_frmaes[geneID][frame]:
				if codon in translation_table:
					protein += translation_table[codon]
					
				else:
					print("O codon não está no dicionário de tradução")
			protein_frames[geneID][frame] = protein		

for geneID in protein_frmaes.keys():
	longestProtein = ""
	longestFrame = ""
	for frame in protein_frames[geneID]:
		proteina = re.findall(r"(M[A-Z]+?)\*", protein_fames[geneID][frame]  #* significa 0 ou mais
		for i in proteinas:
			if  len(i) > len(longestProtein):
				longestProtein = i
				longestFrame = frame
	print(geneID, longestProtein, logestFrame)

with open ("Python_08.translated.aa","w") as outputFile:
	for geneID in codons_frames.keys():
		for frame in protein_frames[geneID]:
			headline = geneId + "_" + frame + "\n"
			outputFile.write(headline)
			#codons = " ".join(codons_frmae[geneID][frame]) + "\n"
			outputFile.write(proteina)
##CDM :  chmod +x Python_08.py
## .\
