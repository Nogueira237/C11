import numpy as np  # importa o numpy

numLinhas = np.random.randint(1, 11)    # numero aleatorio de linhas
numColunas = np.random.randint(1, 11)   # numero aleatorio de colunas
# print(numLinhas, numColunas)

mtz = np.ones([numLinhas, numColunas]) # cria a matriz com as variaveis aleatorias
print(mtz)

nElementos = numLinhas * numColunas    # multiplica linha e coluna
print(nElementos)

if nElementos%2 == 0:
    print(f'A matriz de {nElementos} poderia se tornar um vetor unimensional com número par de elementos.')
else:
    print(f'A matriz de {nElementos} poderia se tornar um vetor unimensional com número impar de elementos.')