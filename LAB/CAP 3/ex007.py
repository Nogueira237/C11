# lista com ingredientes de uma receita de bolo
ingredientes = ['farinha', 'leite', 'ovos', 'fermento', 'açucar']
print(f'Ingredientes da receita {ingredientes}\n')

# converte a lista em conjunto
ingredientes_set = set(ingredientes)

# conjuntos das 2 pessoas
pessoa1 = {'farinha', 'leite', 'ovos'}
pessoa2 = {'farinha', 'manteiga', 'sal'}

# diferença entre os ingredientes necessarios e os disponiveis para cada pessoa
faltamPessoa1 = ingredientes_set - pessoa1
faltamPessoa2 = ingredientes_set - pessoa2

# mostra os ingredientes disponíveis
print(f"Pessoa 1 possui: {pessoa1}")
print(f"Pessoa 2 possui: {pessoa2}\n")

# mostra os ingredientes que faltam
print(f"Faltam para a pessoa 1: {faltamPessoa1}")
print(f"Faltam para a pessoa 2: {faltamPessoa2}\n")