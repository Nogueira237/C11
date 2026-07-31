nome = input('Nome completo: ')

print("Nome em maiusculo:", nome.upper())
print("Nome em minusculo:", nome.lower())
print("Quantidade de letras:", len(nome.replace(" ", "")))

partesNome = nome.split()
nomeDoInatel = nome.replace(partesNome[-1], 'do Inatel')
print("Nome do Inatel:", nomeDoInatel)