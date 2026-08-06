# lista para guardar os dicionarios
produtos = []

# dados para os dicionarios
nome1 = input('Nome produto 1: ')
preco1 = float(input('Preço produto 1: '))
quant1 = int(input('Quantidade produto 1: '))
produto1 = {'nome' : nome1, 'preco' : preco1, 'quant' : quant1}

nome2 = input('Nome produto 2: ')
preco2 = float(input('Preço produto 2: '))
quant2 = int(input('Quantidade produto 2: '))
produto2 = {'nome' : nome2, 'preco' : preco2, 'quant' : quant2}

nome3 = input('Nome produto 3: ')
preco3 = float(input('Preço produto 3: '))
quant3 = int(input('Quantidade produto 3: '))
produto3 = {'nome' : nome3, 'preco' : preco3, 'quant' : quant3}

produtos = [produto1, produto2, produto3]

for p in produtos:
    total = p['preco'] * p['quant']
    print(f"\nNome do produto: {p['nome']}")
    print(f"Valor total em estoque: R${total}")
print()