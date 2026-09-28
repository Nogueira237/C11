# FUNDAMENTOS DE SEABORN
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset tips
ds_tips = sns.load_dataset('tips')
print(ds_tips)

# Setando um estilo diferente no gráfico
sns.set_style('dark')

# Traçando um scatterplot
sns.scatterplot(data=ds_tips, x='total_bill',y='tip')
plt.xlabel('Conta total em US$')
plt.ylabel('Gorjeta em US$')
plt.show()