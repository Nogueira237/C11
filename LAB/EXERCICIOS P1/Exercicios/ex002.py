import numpy as np

dataset = np.loadtxt('LAB/EXERCICIOS P1/DataSets/paises.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai somente as regioes
dataset = dataset[1:, 1]

# regioes e numero de regioes
regioes = np.unique(dataset)
nRegioes = len(regioes)

# mostra o número de regiões e o nome delas
print(f'Número de regiões: {nRegioes}')
for r in regioes:
    print(r)
