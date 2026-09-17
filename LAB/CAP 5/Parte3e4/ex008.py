import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

dfPaises = dfPaises.drop('Coastline (coast/area ratio)', axis=1)    # remove a coluna coastline

dfPaises.to_csv('LAB/CAP 5/DataSets/paises_sem_coastline.csv', index=False) # cria o .csv

print(dfPaises)