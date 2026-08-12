import numpy as np # importa numpy

# Criando array de pares entre 0 a 51
arr1 = np.arange(0, 51, 2)
print(f'Array 1: {arr1}')

# Criando array de pares entre 50 e 100
arr2 = np.arange(50, 100, 2)
print(f'Array 2: {arr2}')

# Somando os arrays
arr3 = np.concatenate([arr1, arr2])
print(f'Arrays concatenados: {arr3}')

