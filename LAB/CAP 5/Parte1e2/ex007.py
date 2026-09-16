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

colunaD = df.loc['D']
mediaD = colunaD.sum() / len(colunaD)
print(mediaD)

colunaE = df.iloc[4, :]
print(colunaE.sum())