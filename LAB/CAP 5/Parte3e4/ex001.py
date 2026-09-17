import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

oceania = dfPaises['Region'].str.contains('OCEANIA')    # verifica se 'Region' = 'OCEANIA'
print(dfPaises[oceania])

print(f'Número de países da Oceania: {len(dfPaises[oceania])}')
#print(sum(oceania))