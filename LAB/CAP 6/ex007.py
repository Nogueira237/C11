import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

europa = ds[ds['Region'].str.strip() == 'WESTERN EUROPE'] # apenas os países da Europa Ocidental

# Cria o gráfico
plt.plot(europa['Country'], europa['GDP ($ per capita)'], label='GDP ($ per capita)')   # label para a legenda

plt.plot(europa['Country'], europa['Phones (per 1000)'], 'r', label='Phones (per 1000)')

plt.xlabel('Países')
plt.ylabel('Valores')

plt.legend()        # legenda no grafico
plt.show()