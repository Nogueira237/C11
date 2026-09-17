import pandas as pd  # importa o pandas

dfPaises = pd.read_csv('LAB/CAP 5/DataSets/paises.csv', delimiter = ';')    # le o dataset 'paises.csv'

# Função que reduz a mortalidade infantil em 15%
def reduzirMortalidade(valor):
    return valor * 0.85

# Aplica a função à coluna
mortalidadeReduzida = dfPaises['Infant mortality (per 1000 births)'].apply(reduzirMortalidade)

# Concatena a coluna original com a coluna resultante
comparacao = pd.concat([
    dfPaises['Infant mortality (per 1000 births)'],
    mortalidadeReduzida
], axis=1)

print(comparacao)