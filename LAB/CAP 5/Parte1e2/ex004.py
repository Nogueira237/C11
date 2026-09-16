import pandas as pd  # importa o pandas

langs1 = ['Java', 'C', 'Python']
versao1 = [16.25, 16.04, 9.85]

seriesAno1 = pd.Series(index = langs1, data = versao1)

langs2 = ['C', 'Python', 'Java']
versao2 = [16.21, 12.12, 11.68]

seriesAno2 = pd.Series(index = langs2, data = versao2)

#print(seriesAno1)
#print(seriesAno2)

diferencaAnos = seriesAno2 - seriesAno1     # negativo -> declínio / positivo -> crescimento
#print(diferencaAnos)

cresceu = diferencaAnos[diferencaAnos > 0]
print(cresceu)