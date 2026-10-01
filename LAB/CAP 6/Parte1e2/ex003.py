import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

ds = pd.read_csv('LAB/CAP 6/DataSets/space.csv', delimiter = ';')    # le o dataset 'paises.csv'

roscosmos = ds[ds['Company Name'] == 'Roscosmos']
print(roscosmos)

success = sum(roscosmos['Status Mission'] == 'Success')
failure = len(roscosmos) - success

plt.pie(x = [success, failure], labels = ['% Sucesso', '% Falha'], autopct = '%1.1f%%')
plt.show()

