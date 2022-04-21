  # Modo mais simples:

from math import factorial

print('Digite um número para')
número = int(input('calcular seu fatorial: '))

print('Fazendo os calculos de {}! que é igual a {}'.format(número, factorial(número)))

  # Modo mais dificil e mais útil ;-; :

número = int(input('Digite um número para saber seu fatorial: '))
contador = número
fatorial = 1

print('Calculando {}! = '.format(número), end='')

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x 'if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print('{}'.format(fatorial))

  # Usando o for:

n = int(input('Digite um número: '))
c = n
f = 1

print('Faznedos os calculos de  {}! '.format(n), end='')

for cont in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))