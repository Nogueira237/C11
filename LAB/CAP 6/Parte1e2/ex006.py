import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/space.csv', delimiter = ';')    # le o dataset 'paises.csv'

ds = ds['Status Rocket'] == 'StatusActive'

active = sum(ds)
retired = len(ds) - active

plt.pie(x = [active, retired], labels = ['% Ativos', '% Desativados'], autopct = '%1.1f%%')

plt.show()