import pandas as pd  # importa o pandas
import numpy as np  # importa o numpy

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

dfPaises = dfPaises.loc[:, ['Country', 'Region', 'Population']]
print(dfPaises)

Population = dfPaises.loc[:, 'Population']

maior = np.argmax(Population)       # acha o indice do maior valor de 'population'

print(f"Nome: {dfPaises['Country'][maior]}")
print(f"Região: {dfPaises['Region'][maior]}")
print(f"População: {dfPaises['Population'][maior]}")