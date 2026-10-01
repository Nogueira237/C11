import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

americaLatina = ds[ds['Region'].str.strip() == 'LATIN AMER. & CARIB']

print(americaLatina)

plt.scatter(americaLatina['GDP ($ per capita)'], americaLatina['Literacy (%)'], s = americaLatina['Population']/10000)
plt.show()