# FUNDAMENTOS DE MATPLOTLIB
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
# Plotando gráficos de linhas com matplotlib (plot)

ds = pd.read_csv('Teorica/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

## BAR PLOT

# Qual a diferença das 5 maiores rendas per capita do dataset?

maioresGDP = ds.nlargest(5, 'GDP ($ per capita)')   # pega os 5 maiores renda per capita
#print(maioresGDP)

plt.bar(maioresGDP['Country'], maioresGDP['GDP ($ per capita)'])    # cria um gráfico de barras

plt.show()
