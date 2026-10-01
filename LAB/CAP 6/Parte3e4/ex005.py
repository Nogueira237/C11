import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset paises.csv
ds = pd.read_csv('LAB/CAP 6/DataSets/paises.csv', sep = ';')
print(ds)

# heatmap
# selecionando as colunas que quero identificar uma correlação
corr = ds[['GDP ($ per capita)', 'Literacy (%)', 'Infant mortality (per 1000 births)', 'Phones (per 1000)']].corr()

sns.heatmap(
    corr,
    annot = True,   # mostrar valores
    fmt = '.2f'     # 2 casas decimais
)

plt.show()