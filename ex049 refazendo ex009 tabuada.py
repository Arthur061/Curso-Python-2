numero = int(input('Digite um número para saber sua tabuada até 10: '))
soma = 0
for c in range(1, 10+1):
    soma = soma + 1
    multiplica = numero * soma
    print('{} x {} = {}'.format(numero, soma, multiplica))