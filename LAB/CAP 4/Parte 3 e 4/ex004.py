import numpy as np

dataset = np.loadtxt('LAB/CAP 4/DataSets/space.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

# extrai a coluna de empresas e custo
dataset = dataset[1:, [1, 6]]

# extrai só as que são da empresa "SpaceX"
missoesSpacex = np.char.find(dataset[:, 0], 'SpaceX') != -1

# extrai a missao mais cara
custosSpaceX = dataset[missoesSpacex, 1].astype(float)
maisCara = np.max(custosSpaceX)
print(f'Custo da missão mais cara: {maisCara:.2f}')