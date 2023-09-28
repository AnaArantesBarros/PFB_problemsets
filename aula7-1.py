taxa = 'sapiens, erectus, neanderthalensis'
#print(taxa,taxa[1],type(taxa))
print(type(taxa))

species = taxa.split(",")
print(species)
print(species[1],type(species))

species.sort()
print(species)
def tamanho(data):
	return len(data)

species.sort(key=tamanho)
print(species)
