import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Importando os datasets
airtravel = pd.read_csv('Teorica/DataSets/airtravel.csv', delimiter = ',', index_col = 'Date', parse_dates = True)
co2emission = pd.read_csv('Teorica/DataSets/co2_emissions.csv', delimiter = ',', index_col = 'Year', parse_dates = True)

# Cria uma dashboard
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Traçando as séries temporais
airtravel['Passengers'].plot(
    ax=axes[0],
    title='Passageiros',
    xlabel='Data',
    ylabel='Número de passageiros'
)


co2emission['CO2_Emissions'].plot(
    ax=axes[1],
    title='Emissão de CO2',
    xlabel='Ano',
    ylabel='Emissão'
)

plt.show()