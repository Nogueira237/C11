import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

dfPaises = dfPaises.loc[:, ['Country', 'Coastline (coast/area ratio)']]     # separa as colunas do dataset

MascaraNoCoast = dfPaises['Coastline (coast/area ratio)'] == 0      # cria uma mascara de true e false para os paises que tem o parametro igual a 0

noCoast = dfPaises[MascaraNoCoast]  # mostra os nomes baseado na condição(mascara criada)

print(noCoast)

noCoast.to_csv('LAB/CAP 5/DataSets/noCoast.csv', index = False) # cria o arquivo