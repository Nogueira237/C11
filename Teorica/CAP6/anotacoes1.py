# FUNDAMENTOS DE MATPLOTLIB
import numpy as np                  # importa numpy
import pandas as pd                 # importa pandas
import matplotlib.pyplot as plt     # importa módulo 'pyploy' do matplotlib

# Plotando gráficos de linhas com matplotlib (plot)
x = np.array([1, 2, 3, 4]) # eixo X

y = x*2 # eixo Y

y2 = x**2 # eixo y 2

# legendas pro eixo x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# plotando gráfico
plt.plot(x, y, '*:r', x, y2, 's--b', linewidth = '3', markersize = '20')     # '*:r' formata o gráfico
plt.show()      # mostra o gráfico na IDE

