# FUNDAMENTOS DE MATPLOTLIB
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
# Plotando gráficos de linhas com matplotlib (plot)

dfPaises = pd.read_csv('Teorica/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

print(dfPaises)