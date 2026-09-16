import pandas as pd  # importa o pandas

langs1 = ['Java', 'C', 'Python']
versao1 = [16.25, 16.04, 9.85]

seriesAno1 = pd.Series(index = langs1, data = versao1)

langs2 = ['C', 'Python', 'Java']
versao2 = [16.21, 12.12, 11.68]

seriesAno2 = pd.Series(index = langs2, data = versao2)

#print(seriesAno1)
#print(seriesAno2)

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print(f"Porcentagem total ano 1: {totalAno1}%")
print(f"Porcentagem total ano 2: {totalAno2}%")