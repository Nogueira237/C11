# FUNDAMENTOS DE SEABORN
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset tips
ds_tips = sns.load_dataset('tips')

# Traçando o regplot
sns.regplot(
    data = ds_tips,
    x = 'total_bill',
    y = 'tip',
    line_kws = {'color':'red'}    # muda a cor da linha
)

plt.show()