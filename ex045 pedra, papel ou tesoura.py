from random import randint
from time import sleep

print('\033[33m -=' * 6)
print('\033[34mJOGUINHO DIVERTIDO')
print('\033[33m -=' * 6)

print('\033[35m[ 0 ] PEDRA \n'
      '[ 1 ] TESOURA \n'
      '[ 2 ] PAPEL')
escolha = int(input('\033[36mDigite a sua escolha: '))

pc_escolha = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

# Se as escolha forem iguais
if escolha == 1 and pc_escolha == 1:
    print('\033[33mOs dois escolheram TESOURA, o resultado foi EMPATE!!')

elif escolha == 0 and pc_escolha == 0:
    print('\033[33mOs dois escolheram PEDRA, o resultado foi EMPATE!!')

elif escolha == 2 and pc_escolha == 2:
    print('\033[33mOs dois escolheram PAPEL, o resultado foi EMPATE!!')

# Se o usuario ganhar
if escolha == 1 and pc_escolha == 2:
    print('\033[33m -=' * 10)
    print('\033[32mVoce venceu!!')
    print('\033[mA sua escolha foi TESOURA e a do computador foi PAPEL')
    print('\033[33m -=' * 10)

elif escolha == 0 and pc_escolha == 1:
    print('\033[33m -=' * 10)
    print('\033[32mVoce venceu!!')
    print('\033[mA sua escolha foi PEDRA e a do computador foi TESOURA')
    print('\033[33m -=' * 10)

elif escolha == 2 and pc_escolha == 0:
    print('\033[33m -=' * 10)
    print('\033[32mVoce venceu!!')
    print('\033[mA sua escolha foi PAPEL e a do computador foi PEDRA')
    print('\033[33m -=' * 10)

# Se o computador ganhar
if pc_escolha == 0 and escolha == 1:
    print('\033[33m -=' * 10)
    print('\033[31mVoce prdeu :((')
    print('\033[mA sua escolha foi TESOURA e a do computador foi PEDRA')
    print('\033[33m -=' * 10)

elif pc_escolha == 1 and escolha == 2:
    print('\033[33m -=' * 10)
    print('\033[31mVoce prdeu :((')
    print('\033[mA sua escolha foi PAPEL e a do computador foi TESOURA')
    print('\033[33m -=' * 10)

elif pc_escolha == 2 and escolha == 0:
    print('\033[33m -=' * 10)
    print('\033[31mVoce prdeu :((')
    print('\033[mA sua escolha foi PEDRA e a do computador foi PAPEL')
    print('\033[33m -=' * 10)