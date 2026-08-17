import numpy as np

# Slicing no numpy
np.random.seed(10)
mtz = np.random.randint(1, 99, 9).reshape(3, 3)
print(mtz)

# Extraindo apenas a segunda linha da matriz
print(mtz[1])

# Extraindo apenas a terceira coluna da matriz
print(mtz[:, 2])

# Extraindo a matriz 2x2 no canto inferior direito da matriz original
print(mtz[1:, 1:])


# Condicionais no numpy
print(mtz)

# Mostra apenas os elementos menores que 70
print(mtz<70)   # true or false (máscara)
print(mtz[mtz<70])   # valor dos elementos

# Retorna apenas os elementos pares
print(mtz%2==0)
print(mtz[mtz%2==0])

# Análise de padrões textuais com numpy
arr = np.array(['Inatel', 'Casa viva', 'ICC', 'CDG', 'eHealth', 'CSILab', 'RobotBulls', 'ProdLab', 'CRA', 'CRR'])
print(arr)

# Submodulo do NumPy para trabalhar com texto: char
# Buscando qual texto aceita um padrão informado
arr = np.char.upper(arr)
print(np.char.find(arr, 'A'))       # retorna o indice do primeiro "a" da palavra ou '-1' se não tiver "a"
print(np.char.find(arr, 'A') >= 0)      # mascara de valores com >= 0 "a"
cond = np.char.find(arr, 'A') >= 0
print(arr[cond])                    # mostra o valor dos elementos da mascara

