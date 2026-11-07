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

# Realizando a decomposição das séries
decompositionAirtravel = seasonal_decompose(airtravel['Passengers'], model='additive')
decompositionAirtravel.plot()
plt.tight_layout()
plt.show()
# Perguntas - Airtravel
# a. Sim, apresenta tendência crescente.
# b. Sim, cresce até o mês 7-8, e depois decresce até o início do outro ano.
# c. Não é possível identificar um ciclo.

decompositionC02 = seasonal_decompose(co2emission['CO2_Emissions'], model='additive')
decompositionC02.plot()
plt.tight_layout()
plt.show()
# Perguntas - C02 emission
# a. Sim, apresenta tendência decrescente.
# b. Não, no gráfico de sazonalidade o marcador fica sempre em zero.
# c. Não é possível identificar um ciclo.