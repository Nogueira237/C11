import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/space.csv', delimiter = ';')    # le o dataset 'paises.csv'

falhas = ds[ds['Status Mission'] == 'Failure']      # pega somente as missoes falhas

cincoMaiores = falhas['Company Name'].value_counts().head(5)    # pega as 5 empresas com mais falhas

plt.bar(cincoMaiores.index, cincoMaiores.values)    # cria o gráfico

plt.xlabel('Empresa')
plt.ylabel('Número de falhas')

plt.show()
