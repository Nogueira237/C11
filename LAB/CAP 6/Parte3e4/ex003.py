import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib
import seaborn as sns               # importa seaborn

# Importando o dataset titanic
ds_titanic = sns.load_dataset('titanic')
print(ds_titanic)

# boxplot
sns.boxplot(
    data = ds_titanic, # dataset
    x = 'pclass',
    y = 'age',
    hue = 'sex' # separa por sexo
)

plt.show()