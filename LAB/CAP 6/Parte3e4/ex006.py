import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset paises.csv
ds = pd.read_csv('LAB/CAP 6/DataSets/paises.csv', sep =';')
#print(ds)

ds['Region'] = ds['Region'].str.strip()     # remove espaços em branco do começo e final do texto

regioes = ds[ds['Region'].isin(['LATIN AMER. & CARIB', 'WESTERN EUROPE'])]

plt.figure(figsize=(10, 6))
# boxplot
sns.boxplot(
    data = regioes,
    x = 'Region',
    y = 'GDP ($ per capita)'
)

plt.show()