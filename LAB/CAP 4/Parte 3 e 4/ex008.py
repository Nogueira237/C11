import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai coluna de nome e custo
dataset = dataset[1:, [1, 6]]

# coluna de custo
custosMissoes = dataset[:, 1].astype(float)

# incide do maior valor
indice = np.argmax(custosMissoes)

# armazena nome e custo 
empresa = dataset[indice, 0]
valor = custosMissoes[indice]

# mostra as informações
print(f'Empresa: {empresa}')
print(f'Valor: {valor:.2f}')