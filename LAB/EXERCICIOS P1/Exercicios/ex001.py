import numpy as np

dataset = np.loadtxt('LAB/EXERCICIOS P1/DataSets/paises.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# mostra -> pais|regiao|população|area
dataset = dataset[1:, :4]

print(dataset)

# pais, regiao, pop, area = dataset

#for p, r, p, a in zip(pais, regiao, pop, area):
#    print(f'País: {p}')
#    print(f'Região: {r}')
#    print(f'População: {p}')
#    print(f'Área: {a}\n')