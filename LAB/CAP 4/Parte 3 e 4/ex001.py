import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')
#print(dataset)

# Extrai a coluna de "Status Mission"
dataset = dataset[1:,7]
print(dataset)      # mascara

# Gera uma mascara com true e false
mascara = dataset == 'Success'

# soma os trues e divide pelo tamanho do dataset
media = np.sum(mascara) / len(dataset) * 100
print(media)