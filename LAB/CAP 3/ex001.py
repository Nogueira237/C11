# Tupla - imutavel / nomes = (‘Goku’, ‘Vegeta’, ‘Trunks’, ‘Gohan’)
# Listas - mutavel / nomes = [‘Goku’, ‘Vegeta’, ‘Trunks’, ‘Gohan’]
# Conjuntos - NÃO ORDENADA e NÃO ADMITE ELEMENTOS DUPLICADOS / nomes = {‘Goku’, ‘Vegeta’, ‘Trunks’, ‘Gohan’, ‘Trunks’, ‘Goku’}
# Dicionarios - MUTÁVEIS e (CHAVE:VALOR) / dados = {‘nome’: ‘Goku’, ‘idade’: 43}

# 5 primeiros colocados
classificacao = ['Cruzeiro','Palmeiras','Flamengo','Barcelona','Vasco']     # list para ser imutavel/manter a ordem

print(classificacao[:3])   # Apenas os 3 primeiros colocados = 'Cruzeiro','Palmeiras','Flamengo'
print(classificacao[3:])    # Os últimos 2 colocados = ['Barcelona', 'Vasco']
print(sorted(classificacao)) # Uma lista com os times em ordem alfabética = ['Barcelona', 'Cruzeiro', 'Flamengo', 'Palmeiras', 'Vasco']
print(classificacao.index("Barcelona") + 1) # Em que posição da tabela se encontra o Barcelona = 4