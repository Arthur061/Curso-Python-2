numero = contador = soma = 0
numero = int(input('Digite um número [999 para parar]: '))

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))

print('Acabou')
print('Voce digitou {} números'.format(contador))
print('A soma dos números é {}'.format(soma))
