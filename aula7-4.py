#lista = [item for item in range(0,100)]
#print(lista)

data = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
"""for d in data:
	print(len(d),'	',d)"""
#tupla =(len(item),item) for item in data)
lista = [(len(item),item) for item in data]
print(lista)
