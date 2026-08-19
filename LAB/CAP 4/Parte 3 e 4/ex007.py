import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai coluna de location
dataset = dataset[1:, 2]

# mascara de true
contemRussia = np.char.find(dataset, 'Russia') != -1

# conta o total de missoes lançadas em localizações que contém 'Russia'
total = np.sum(contemRussia)
print(f'Total de missões lançadas na Russia: {total}')