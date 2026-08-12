import numpy as np  # importa o numpy

# Cria um array só de números 1 com 8 posições
arr1 = np.ones(8)
print(f'Array 1: {arr1}')

# Cria um array com 8 elementos aleatórios
arr2 = np.random.randint(0, 10, 8)
print(f'Array 2: {arr2}')

# Soma os dois arrays criados
arr3 = arr1 + arr2
print(f'Array soma: {arr3}')

total = arr3.sum(axis=0)        # armazena a soma dos elementos do arr3
print(f'Soma do array: {total}')    # mostra o valor total da soma do arr3

print("Array remodelado:")
if total >= 40:
    print(arr3.reshape(4, 2))   # mais linhas do que colunas
    
else:
    print(arr3.reshape(2, 4))   # mais colunas do que linhas