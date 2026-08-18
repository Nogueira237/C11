import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# Extraindo a coluna "Cost"
dataset = dataset[1:, 6].astype(float)   # astype converte para float

# mascara de valores > 0
maiorQueZero = dataset > 0

# valores maiores que zero
gastos = dataset[maiorQueZero]

# media dos valores
media = np.sum(gastos) / len(gastos)
print(f"A média dos vaores é: {media:.2f}")