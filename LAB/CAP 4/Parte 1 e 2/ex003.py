import numpy as np  # importa o numpy

# cria matriz 2x2 só de zeros
mtz = np.zeros([2, 2])
print(mtz)

# adicionando número 1 em uma posição aleatória da matriz
linhaRand = np.random.randint(0,2)  # linha aleatoria entre 0 e 1
# print(linhaRand)

colunaRand = np.random.randint(0,2) # coluna aleatoria entre 0 e 1
# print(colunaRand)

mtz[linhaRand][colunaRand] = 1      # muda o elemento na linha e coluna sorteada para 1
print(mtz)

# jogando
vitoria = 0          # precisa de 3 pra vencer
for i in range(3):   # 3 jogadas
    linhaSelecionada = int(input('Selecione uma linha [0/1]: '))    # jogador seleciona linha
    colunaSelecionada = int(input('Selecione uma coluna [0/1]: '))  # jogador seleciona coluna

    if mtz[linhaSelecionada][colunaSelecionada] == 1:               # se acertou a bomba
        print('Game Over! :( Try Again!')
        break   # interrompe o for
    else:
        vitoria += 1

    if vitoria == 3:    # condição para ganhar
        print('Congratulations! You beat the game!')

    
    