import numpy as np

colors = [
{"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
{"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
{"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
{"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}}
]

# a. Mostre apenas o nome das cores que são primárias;

print('Cores primárias')
for cor in colors:
    if cor['type'] == "primary":
        print(cor['color'])

# b. Mostre apenas os códigos hexadecimais das cores que possuem tom de azul máximo (255);

print('Tom de azul máximo')
for cor in colors:
    if cor['code']['rgba'][2] == 255:
        print(cor['code']['hex'])

# c. A partir da coleção colors, extraia seus valores para criar um NumPy Array 1-D formado apenas pelo nome e código hexadecimal de cada cor; Ex: “black”, ”#000”, “green”, “#0F0”...

arr = []
for cor in colors:
    nome = cor['color']
    hexa = cor['code']['hex']
    arr.append(nome)
    arr.append(hexa)

print(arr)

# d. Transforme o Array 1-D em um Array 2-D no seguinte padrão:
# ...
# green #0F0
# yellow #FF0
# ...

arr = np.array(arr, dtype=object)   # array estava com o tipo definido '<U6' e estava cortando a palavra 'amarelo' para 'amarel, entao foi definido um tipo na criação do array
arr = arr.reshape(4, 2)
print(arr)

# e. Troque o nome de cada cor no Array 2-D para seu respectivo nome em Português;
arr[0][0] = 'Preto'
arr[1][0] = 'Verde'
arr[2][0] = 'Amarelo'
arr[3][0] = 'Azul'
print(arr)
 