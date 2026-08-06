# lista de pessoas
pessoas = []

# le os 3 nomes e respectivos pesos
for i in range(3):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    peso = input(f"Digite o peso da {i+1} pessoa: ")
    pessoas.append([nome, peso])

# atribui pesos iniciais
mais_pesada = pessoas[0]
mais_leve = pessoas[0]

# varre a lista
for pessoa in pessoas:
    if pessoa[1] > mais_pesada[1]:
        mais_pesada = pessoa

    if pessoa[1] < mais_leve[1]:
        mais_leve = pessoa

print(f"Pessoa mais pesada: {mais_pesada[0]}, com {mais_pesada[1]}kg")
print(f"Pessoa mais leve: {mais_leve[0]}, com {mais_leve[1]}kg")
