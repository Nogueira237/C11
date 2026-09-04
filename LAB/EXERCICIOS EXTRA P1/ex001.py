control = 'Y'
musicas = []

while control == 'Y':
    nome = input('Nome da música: ')
    ano = int(input('Ano da música: '))
    song = {'nome:': nome, 'ano': ano}
    musicas.append(song)
    control = input('Deseja adicionar outra música? [Y/N]')

# a. Quantas músicas foram cadastradas;
print(f"Número de músicas cadastradas: {len(musicas)}")

# b. As Informações da(s) música(s) do ano mais antigo; 
antiga =  min(musicas, key=lambda musica: musica['ano'])
print(f"A música mais antiga é: {antiga}")