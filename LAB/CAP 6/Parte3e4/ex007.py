import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset paises.csv
ds = pd.read_csv('LAB/CAP 6/DataSets/paises.csv', sep =';')
#print(ds)

# regplot
sns.regplot(
    data = ds,
    x = 'Literacy (%)',
    y = 'Infant mortality (per 1000 births)',
    line_kws = {'color':'red'}  # muda a cor da linha
)

plt.show()