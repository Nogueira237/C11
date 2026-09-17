import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

estatisticas = dfPaises.groupby('Region')['Population'].describe()  # groupby('Region') agrupa os paises pela regiao, ['Population'].describe() calcula as estatisticas

print(estatisticas.head())  # .head() mostra apenas as 5 primeiras linhas do resultado