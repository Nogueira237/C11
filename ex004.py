dist = int(input('Qual a distância da viagem em km? '))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print('O preço da passagem é R$' + str(preco))