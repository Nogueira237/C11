import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

dfPaises = dfPaises.loc[:, ['Country', 'Region', 'Literacy (%)']]

agrupaRegioes = dfPaises.groupby('Region')['Literacy (%)'].mean()   # groupby('Region') junta as regioes, ['Literacy (%)'].mean() calcula a média de cada grupo

print(agrupaRegioes)