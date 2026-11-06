import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregando o dataset do Índice de Volume de Vendas no Setor Varejista Brasileiro
dataset = pd.read_csv('Teorica/DataSets/retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)

# Decomposição aditiva
decomposition = seasonal_decompose(dataset['retail_index'], model='additive')

# Plotando os componentes
decomposition.plot()
plt.tight_layout()
plt.show()