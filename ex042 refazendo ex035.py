print('\033[33m-=' * 20)
print('\033[31mAnalisando um triangulo')
print('\033[33m-=' * 20)
r1 = float(input('\033[35mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Parte nova é as que estão sem cor!

if r1 == r2 and r1 == r3:
    print('Esse triangulo é um triangulo EQUILÁTERO')
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
    print('Esse triangulo é um triangulo ISÓSCELES')
elif r1 != r2 and r1 != r3 and r3 != r2:
    print('Esse triangulo é um triangulo ESCALENO')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[31mOs segmentos acima PODEM formar um triangulo !!')
else:
    print('\033[31mOs segmentos acima NÃO podem formar um triangulo !!')
