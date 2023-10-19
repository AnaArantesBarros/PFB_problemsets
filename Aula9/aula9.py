
DNA = set('AGGCT')
seq = 'AGGCT'
nt_comp = {}
for base in DNA:
        nt_comp[base] = seq.count(base)
        print(f'A quantidade da base {base} é {seq.count(base)}')
GC = (nt_comp['G'] + nt_comp['C'] )/ len(seq)
print(f'A quantidade de GC é de {GC} %.')        


        

