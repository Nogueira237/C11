import numpy as np

# a. Crie dois NumPy Arrays 1-D com 4 nomes de pessoas cada;
arr1 = ['Ana', 'Benício', 'Carlos', 'Diana']
arr2 = ['Eduardo', 'Felipe', 'Gabriela', 'Hildo']

# b. Em seguida, concatene-os em um só Array;
arr3 = np.concatenate((arr1, arr2))
print(arr3)

# c. Transforme o Array final em um Array 2-D com mais colunas do que linhas;
arr3 = arr3.reshape(2, 4)
print(arr3)

# d. Por fim, ordene os nomes do Array 2-D em ordem decrescente;
arr3 = np.sort(arr3.flatten())[::-1].reshape(2, 4)
print(arr3)
