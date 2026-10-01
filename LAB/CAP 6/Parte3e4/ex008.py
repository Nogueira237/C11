import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset space.csv
ds = pd.read_csv('LAB/CAP 6/DataSets/space.csv', sep =';')
#print(ds)

# filtra as missoes com cost > 0
ds = ds[ds[' Cost'] > 0]
#print(ds)

sns.boxplot(
    data = ds,
    x = 'Status Mission',
    y = ' Cost'
)

plt.show()