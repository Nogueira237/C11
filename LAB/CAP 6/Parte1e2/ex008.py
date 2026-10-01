import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/space.csv', delimiter = ';')    # le o dataset 'paises.csv'

# 5 empresas com mais missões de sucesso
sucesso = ds[ds['Status Mission'] == 'Success']
cincoSucesso = sucesso['Company Name'].value_counts().head(5)

# 5 empresas com mais missões de falha
falha = ds[ds['Status Mission'] == 'Failure']
cincoFalha = falha['Company Name'].value_counts().head(5)

# gráfico da esquerda - Sucesso
plt.subplot(1, 2, 1)
plt.bar(cincoSucesso.index, cincoSucesso.values)
plt.xlabel('Empresa')
plt.ylabel('Número de missões')

# gráfico da direita - Falha
plt.subplot(1, 2, 2)
plt.bar(cincoFalha.index, cincoFalha.values)
plt.xlabel('Empresa')
plt.ylabel('Número de missões')

plt.show()