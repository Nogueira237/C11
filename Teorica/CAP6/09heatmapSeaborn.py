# FUNDAMENTOS DE SEABORN
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset tips
ds_tips = sns.load_dataset('tips')

# Traçando o heat map
# selecionando as colunas que quero identificar uma correlação
corr = ds_tips[['total_bill', 'tip', 'size']].corr()

# Traçando o heatmap
sns.heatmap(
    corr,
    annot = True, # mostrar valores
    fmt = '.2f'     # 2 casas decimais
)

plt.show()