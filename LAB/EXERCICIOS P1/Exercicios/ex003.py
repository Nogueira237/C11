import numpy as np

dataset = np.loadtxt('LAB/EXERCICIOS P1/DataSets/paises.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai a coluna literacy
dataset = dataset[1:, 9].astype(float)  # 'astype' converte para o tipo escolhido

# usa 'sum' para somar todos os valores do dataset
total = np.sum(dataset)

# calcula e mostra a media
media = total / len(dataset)
print(f'Média: {media:.2f}%')