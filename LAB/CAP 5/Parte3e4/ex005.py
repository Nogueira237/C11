import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

def ajudaHumanitaria(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'

dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(ajudaHumanitaria)       # cria o campo 'Humanitarian Help'

print(dfPaises)