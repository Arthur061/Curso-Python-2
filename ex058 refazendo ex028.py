from random import randint
from time import sleep

computador = randint(0, 10) #Faz o computador 'PENSAR'

print('\033[33m-=-' * 20)

print('\033[36mPensei em um número...')

jogador = int(input('\033[34mO computador pensou em um número de 0 a 10, tente adivinha!! Digite seu número: ')) #O jogador tenta adivinhar

print('\033[33m-=-' * 20)
print('')

print('\033[33mPROCESSANDO')
sleep(3)

  # Parte melhorada:

while jogador != computador:
    print('\033[31mOpção incorreta, tente novamente: ')
    jogador = int(input('\033[mDigite um novo número: '))

    if jogador > computador:
        print('O número escolhido por voce é maior que o escolhido pelo computador! ')

    elif jogador == computador:
        print('Depois de {} tentativas voce conseguiu!! '.format(jogador))
        print(' ')

    else:
        print('O número escolhido por voce é menor que  o escolhido pelo computador! ')

  # Parte melhora termina aqui

if jogador == computador:
    print('\033[32mBoa, voce acertou o número')

else:
    print('\033[31mTa de boa boy, o computador é foda também. Pensei no número {} não no {}'.format(computador, jogador))

