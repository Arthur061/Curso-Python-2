soma = 0
num = 0
contador = 0
for c in range(0, 6):
    num = num + 1
    x = int(input('Digite o {}° número: '.format(num)))
    if x % 2 == 0:
        soma += x
        contador += 1
print('Voce informou {} números PARES e a soma deles é {}'.format(contador,soma))