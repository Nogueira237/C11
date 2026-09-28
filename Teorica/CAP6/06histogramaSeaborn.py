# FUNDAMENTOS DE SEABORN
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset penguins
ds_penguins = sns.load_dataset('penguins')
print(ds_penguins.columns)

# Traçando o histograma
sns.histplot(
    data = ds_penguins, # passando o dataset
    x = 'flipper_length_mm',
    hue = 'species', # separa em espécies
    kde = 'True'    # traça um gráfico em linha
)

plt.show()

# histograma tem intervalos, gráfico em barras tem valores exatos