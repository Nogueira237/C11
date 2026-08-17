import numpy as np

dataset = np.loadtxt('../DataSets/space.csv', delimiter = ';', dtype = 'str', encoding='utf-8')
print(dataset)

# Extraindo as colunas do dataset
print(dataset[0,:])

# Extraindo o nome unico das empresas
print(np.unique(dataset[1:, 0]))