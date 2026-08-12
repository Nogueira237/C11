import numpy as np  # importa o numpy

# pegando 16 números aleatórios
np.random.seed(10)
arr = np.random.randint(1, 51, 16)
print(arr)

mtz = arr.reshape(4,4)  # torna o array unidimensional em matriz 4x4
print(mtz)

# media de cada linha       [axis = 1]
medLinhas = mtz.sum(axis=1)/4
print(f'Média de cada linha:{medLinhas}')

# media de cada coluna       [axis = 0]
medColunas = mtz.sum(axis=0)/4
print(f'Média de cada coluna:{medColunas}')

# maior valor das linhas
print(f'Maior valor da média das linhas: {np.max(medLinhas)}')

# maior valor das linhas
print(f'Maior valor da média das colunas: {np.max(medColunas)}')

# contando elementos únicos
numeros, quantidades = np.unique(mtz, return_counts=True)
print('')
print(f'Números: {numeros}')
print(f'Quantidade: {quantidades}')

# numeros que aparecem 2 vezes
print('')
print(f'Números que aparecem duas vezes: {numeros[quantidades == 2]}')