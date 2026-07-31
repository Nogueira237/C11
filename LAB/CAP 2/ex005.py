numero = int(input('Digite um numero: '))

while numero < 1000 or numero > 9999:
    print('Numero invalido. Digite novamente.')
    numero = int(input('Digite um numero:'))

partesNumero = str(numero)

print("Milhar:", partesNumero[0])
print("Centena:", partesNumero[1])
print("Dezena:", partesNumero[2])
print("Unidade:", partesNumero[3])