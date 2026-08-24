import numpy as np

dataset = np.loadtxt('LAB/EXERCICIOS P1/DataSets/paises.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai coluna pais e regiao
dataset = dataset[1:, [0, 1, 8]]

# renda per capita
rendaCap = dataset[:, 2].astype(float)

# indice do valor maximo de renda per capita
indice = np.argmax(rendaCap)

# armazena o nome do pais e a renda per capita
pais = dataset[indice, 0]
rendaMax = rendaCap[indice]

# mostra as informações
print(f'Nome do País: {pais}\nRenda per capita: {rendaMax:.2f}')