# le os dados do aluno
nome = input('Nome do aluno: ')
media = int(input('Média do aluno: '))

# guarda em um dicionario
dadosAluno = {'nome': nome, 'media': media, 'situacao' : 'desconhecida'}

# verifica se esta na media
if(dadosAluno['media'] >= 50):
    situacao = 'AP'
else:
    situacao = 'RP'

# alterna a chave 'situacao' com a aprovação ou reprovação
dadosAluno['situacao'] = situacao

# mostra os dados do aluno
print(dadosAluno)