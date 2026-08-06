# Conjunto samsung
loja1 = {'Galaxy S26 Ultra', 'Iphone 15', 'Galaxy Tab S10', 'Moto G3', 'Galaxy S20 FE'}

#conjunto apple
loja2 = {'Iphone 17 Pro Max', 'Poco X7', 'Redmi note 14', 'Galaxy S20 FE'}

# modelos disponineis
todosModelos = loja1 | loja2

# modelos nas 2 lojas
ambasModelos = loja1 & loja2

# saidas
print('Disponíveis na loja 1:', loja1)
print('Disponíveis na loja 2:', loja2)
print('Todos os modelos disponíveis:', todosModelos)
print('Modelos disponíveis nas 2 lojas:', ambasModelos)
