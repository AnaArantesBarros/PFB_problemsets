favoritos = ['chocolate','final de semana','cachorro','piscina','passear']
print(favoritos, favoritos[int(len(favoritos)/2)])

favoritos[int(len(favoritos)/2)] = 'song bird'
print(favoritos, favoritos[int(len(favoritos)/2)])

favoritos.append('jogos')
favoritos.insert(0,'python')
favoritos.insert(3,'dados')

print(favoritos)

favoritos.pop(len(favoritos)-1)
favoritos.pop(0)
favoritos.pop(4)
print(favoritos)

print(','.join(favoritos))

