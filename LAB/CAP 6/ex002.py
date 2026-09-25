import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/space.csv', delimiter = ';')    # le o dataset 'paises.csv'

ds = ds.drop_duplicates(subset='Company Name')  # e tira os duplicados

usa = ds['Location'].str.contains('USA', na=False).shape[0]     # pega as empresas do eua
china = ds[ds['Location'].str.contains('China', na=False)].shape[0]  # pega as empresas da china

plt.bar(['EUA', 'China'], [usa, china])
plt.show()


