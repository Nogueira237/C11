import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Teorica/DataSets/retail_index_br.csv', delimiter = ';', index_col = 'date', parse_dates = True)

# Transformando os dados de y em float
dataset['retail_index'].astype(float)

# Plotando a Time Series
dataset['retail_index'].plot(figsize=(8,6), title='Índice de volume de vendas no setor varejista brasileiro', xlabel='Data', ylabel='Índice', x_compat =True)

plt.show()