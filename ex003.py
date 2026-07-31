sexo = input('Digite seu sexo [M/F]: ')

while sexo != 'M' and sexo != 'F':
    print('Sexo invalido. Digite novamente.')
    sexo = input('Digite seu sexo [M/F]: ')

if(sexo == 'M'):
    print('Sexo masculino.')
else:
    print('Sexo feminino.')