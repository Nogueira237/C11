# FUNDAMENTOS DE SEABORN
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset tips
ds_tips = sns.load_dataset('tips')

# Traçando um boxplot
sns.boxplot(
    data = ds_tips,
    x = 'day',
    y = 'tip',
    hue = 'sex' # separa por sexo
)

plt.show()