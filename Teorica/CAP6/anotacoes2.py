# FUNDAMENTOS DE MATPLOTLIB
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
# Plotando gráficos de linhas com matplotlib (plot)

ds = pd.read_csv('Teorica/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

# print(ds.columns)

# Quao dispersas estao as rendas per capita dos 6 maiores paises do mundo?

# pegando apenas os 6 maiores paises do planeta
maioresPaises = ds.nlargest(6, 'Area (sq. mi.)')
#print(maioresPaises)


# Traçando o grafico com as rendas per capita desses paises
plt.scatter(maioresPaises['Country'], maioresPaises['GDP ($ per capita)'], s = maioresPaises['Area (sq. mi.)']/10000)  # plt.scatter([linha], [coluna], s)
# o parametro s permite adicionar uma terceira dimensao neste grafico, neste caso dividiu o parametro area por 10000^^

plt.show()