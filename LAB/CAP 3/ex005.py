# le os dados
pessoas = []
n = int(input('Quantas pessoas serão inseridas: '))

for i in range(n):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    idade = int(input(f"Digite a idade da {i+1} pessoa: "))
    sexo = input(f"Digite o sexo da {i+1} pessoa [M/F]: ")
    pessoas.append([nome, idade, sexo])

# calculando e mostrando media da idade do grupo
total = 0
for i in range(n):
    total += pessoas[i][1]

media = total/n
print('Média de idade do grupo:', media)

# calculando mulheres com menos de 20 anos
menosVinte = 0
for i in range(n):
    if pessoas[i][2] == 'F' and pessoas[i][1] < 20:
        menosVinte += 1

# mostrando resultados
print(f'Média de idade do grupo: {media}')
print(f'Mulheres com menos de vinte anos no grupo: {menosVinte}')

