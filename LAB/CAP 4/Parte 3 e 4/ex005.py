import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai o nome das empresas
dataset = dataset[1:, 1]

# conjunto que retorna o nome das empresas e a quantidade de vezes que aparecem
empresas, quantidade = np.unique(dataset, return_counts = True) # zip junta os elementos

for empresa, qtd in zip(empresas, quantidade):
    print(f'Empresa: {empresa} -> {qtd} missões')