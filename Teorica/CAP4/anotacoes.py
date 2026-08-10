# Criando um NumPy Array

# importantando o numpy
import numpy as np

# criando um numpy array de 1D
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
print(type(arr))        # verifica tipo da variavel 'arr'
print(f'Tamanho do array: {arr.size}')     # tamanho do array
print(f'Dimensões do array: {arr.ndim}')     # quantas dimensoes
print(f'Formato do array: {arr.shape}')    # formato do array

# criando um numpy array de 2D
mtz = np.array([10, 20], [30, 40], [50, 60])
print(mtz)
print(f'Tamanho da matriz: {mtz.size}')     # tamanho da matriz
print(f'Dimensões da matriz: {mtz.ndim}')     # quantas dimensoes
print(f'Formato da matriz: {mtz.shape}')    # formato da matriz

#
# Funções pré-prontas para estruturarmos numpy arrays
# Matriz de ones
mtz = np.ones([5, 5])
print(mtz)

# Array de zeros
arr = np.zeros(10)
print(arr)

# Transformando array em matriz
print(arr.reshape(5, 2))

# Arange (alcance do array)
mtz = np.arange(2, 21, 2)   # começa em 2(inclusive), vai até 21(<21), pulando de 2 em 2
print(mtz)
# reshape
print(mtz.reshape(2, 5))

#
# Operações entre numpy arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([60, 40, 20, 10, 5])
arr3 = arr1 + arr2

print(arr1 + arr2)  # soma elemento 1 de arr1 com elemento 1 de arr2, etc...
print(arr1 - arr2)  # subtrai
print(arr1 * arr2)  # multiplica

# Concatenação de arrays
arr3 = np.concatenate([arr1, arr2])
print(arr3)

# Multiplicando ESCALAR por ARRAY - Broadcasting
print(5 * arr3)     

# Estruturando uma matriz com contas
mtz = np.arange(10, 96, 5)
mtz = mtz.reshape(3, 6)    # reshape da matriz para 3 linhas e 6 colunas
print(mtz)

# Extraindo a soma da 1ª coluna
print(mtz.sum(axis=0))          # retorna a soma de cada coluna da matriz
print(mtz.sum(axis=0)[0])       # retorna a soma da coluna de índice 0 (coluna 1)

# Extraindo a soma da 2ª linha
print(mtz.sum(axis=1))          # retorna a soma de cada linha da matriz
print(mtz.sum(axis=1)[1])       # retorna a soma da linha de índice 1 (linha 2)

#
# Números aleatórios com NumPy - Módulo Random
arr = np.random.randint(10)     # numero aleatorio de 0 a 9
print(arr)

arr = np.random.randint(5, 10)  # numero aleatorio de 5 a 9
print(arr)

arr = np.random.randint(1, 10, 10) # 10 numeros aleatorio de 1 a 9
print(arr)

# Plantando a semente aleatória - para gerar os mesmos números independente da máquina
np.random.seed(5)
arr = np.random.randint(1, 10, 10)
print(arr)

#
# Extraindo elementos únicos
print(np.unique(arr))   # extrai os elementos únicos e organiza em ordem crescente

# Contando elementos únicos
print(np.unique(arr, return_counts=True))   # extrai os elementos unicos e mostra quantas vezes eles se repetem