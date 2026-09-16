# importando o numpy e o pandas
import numpy as np
import pandas as pd

# plantando uma semente aleatória
np.random.seed(10)

# criando um dataframe
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

# valores menores que 30 na coluna 'X'
menorQue30 = df['X'] < 30

media = df['X'][menorQue30].sum() / menorQue30.sum()

print(f"Média: {media}")