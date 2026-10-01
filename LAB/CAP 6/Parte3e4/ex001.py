import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset iris
ds_iris = sns.load_dataset('iris')
#print(ds_iris)

setosa = ds_iris[ds_iris['species'] == 'setosa']

# apenas as variáveis numéricas
variaveis = setosa.select_dtypes(include='number')

# calcular correlação
corr = variaveis.corr()
print(corr)

# mapa de calor com a correlação
sns.heatmap(
    corr,
    annot = True, # mostrar valores
    fmt = '.2f'     # 2 casas decimais
)

plt.show()
