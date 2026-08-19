import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai coluna status rocket
dataset = dataset[1:, 5]

# mascara que verifica se é "StatusRetired"
status = np.char.find(dataset, 'StatusRetired') != -1
print(status)

# soma o total de trues
total = np.sum(status)

# faz a media em porcentagem
media = total / len(status) * 100
print(f'{media:.2f}%')