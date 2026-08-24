import numpy as np

dataset = np.loadtxt('LAB/EXERCICIOS P1/DataSets/paises.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai a coluna de regioes
dataset = dataset[1:, 1]

# 
regioes = np.char.find(dataset, 'NORTHERN AMERICA') != -1

print(f'Total de países da America do Norte: {sum(regioes)}')