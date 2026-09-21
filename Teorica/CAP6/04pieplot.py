# FUNDAMENTOS DE MATPLOTLIB
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
# Plotando gráficos de linhas com matplotlib (plot)

ds = pd.read_csv('Teorica/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

## PIE PLOT

paisesSemCosta = ds[ds['Coastline (coast/area ratio)'] == 0]        # paises com condicional de nao ter costa
#print(paisesSemCosta)

qtSemCosta = len(paisesSemCosta)
qtComCosta = len(ds) - qtSemCosta

plt.pie(x = [qtSemCosta, qtComCosta], labels = ['% países sem costa', '% países com costa'])

plt.show()