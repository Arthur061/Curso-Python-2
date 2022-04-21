from random import randint
print('~' * 30)
print('JOGO DO PAR OU ÍMPAR')
print('~' * 30)

vitoria = 0

while True:
    numero = int(input('Digite um número: '))  # Número para calculo
    escolha = str(input('Escolha par ou ímpar: [P / I] ')).upper().split()[0]  # Escolhe Par ou Ímpar
    computador = randint(0, 10)  # Computador pensa em um número entre 0 e 10
    total = computador + numero

    while escolha not in 'PI':
        escolha = str(input('Escolha par ou ímpar: [P / I] ')).upper().split()[0]

    if escolha == 'P':  # Seu usuario escolher Par e ganhar:
        if total % 2 == 0:
            print('-' * 25)
            print(f'Você ganhou!! O computador escolheu {computador} e você {numero}, totalizando {total} que é PAR')
            print('Jogue novamente: ')
            print('-' * 25)
            vitoria += 1

        else:  # Se o usuario escolher Par e perder
            print(f'Você perdeu :( O computador escolheu {computador} e você {numero}, totalizando {total} que é ÍMPAR')
            break

    elif escolha == 'I':  # Se o usuario escolher ímpar e ganhar
        if total % 2 == 1 or total % 5 == 0:
            print('-' * 25)
            print(f'Você ganhou!! O computador escolheu {computador} e você {numero}, totalizando {total} que é ÍMPAR')
            print('Jogue novamente: ')
            print('-' * 25)
            vitoria += 1

        else:  # Se o usuario escolher Ímpar e perder
            print('-' * 25)
            print(f'Você perdeu :( O computador escolheu {computador} e você {numero}, totalizando {total} que é PAR')
            print('-' * 25)
            break

print('')
print('Obrigado por jogar :)')
print('')
print(f'GAME OVERR!! Você ganhou {vitoria} vezes')
