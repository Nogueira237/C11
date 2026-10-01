import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset mpg
ds_mpg = sns.load_dataset('mpg')
print(ds_mpg)

# scatterplot
sns.scatterplot(data = ds_mpg, x = 'horsepower', y = 'mpg')
plt.xlabel('Potência dos veículos')
plt.ylabel('Consumo de combustível')
plt.show()