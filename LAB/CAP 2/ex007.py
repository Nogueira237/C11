palavra = input("Digite uma palavra: ")

vogais = 0
temA = False

for letra in palavra:
    print(letra.upper())

    if letra.lower() in "aeiou":
        vogais += 1

    if letra.lower() == "a":
        temA = True

print("Quantidade de vogais:", vogais)

if temA:
    print("A letra A aparece.")
else:
    print("A letra A não aparece.")