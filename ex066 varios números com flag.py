numero = soma = 0
contador = 0

while True:
    numero = int(input('Digite um número [ 999 para parar ]: '))

    if numero == 999:
        break

    contador += 1
    soma += numero
print(f'Você digitou {contador} valores e a soma deles é {soma}')
