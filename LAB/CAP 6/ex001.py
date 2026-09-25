import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

ds['Region'] = ds['Region'].str.strip()     # remove espaços em branco do começo e final do texto

ds = ds[ds['Region'] == 'NORTHERN AMERICA']


#print(ds)

paises = ds['Country']
mortalidade = ds['Deathrate']
natalidade = ds['Birthrate']

#print(paises)

# criando dashboard
plt.subplot(1, 2, 1)
plt.plot(paises, mortalidade, 'r')
plt.xlabel('País')
plt.ylabel('Taxa de mortalidade')

plt.subplot(1, 2, 2)
plt.plot(paises, natalidade)
plt.xlabel('País')
plt.ylabel('Taxa de natalidade')

plt.show()