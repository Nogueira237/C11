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

# slicing
df = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(df)

# soma de cada linha
print("===== Soma de cada linha =====")
print(df.sum(axis=1))

# soma de cada coluna
print("===== Soma de cada coluna =====")
print(df.sum(axis=0))
