import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai a localizao da missao
dataset = dataset[1:, 2]

# mascara de true e false
mascara = np.char.find(dataset, "USA") != -1

# total de missões realizadas pelos USA
total = np.sum(mascara)
print(total)