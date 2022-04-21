from time import sleep
n1 = int(input('Digite um número inteiro: '))  # Escolha primeiro números
n2 = int(input('Digite mais um número inteiro: '))  # Escolha segundo número

n0 = 0

while n0 != 5:
    print(' ')
    print('números escolhidos são {} e {}'.format(n1, n2))
    print(' ')
    print('Escolha uma das opções abaixo, na qual deseja aplicar os números digitados: \n'
          '\n  [ 1 ]- Soma\n'
          '  [ 2 ]- Multiplicação\n'
          '  [ 3 ]- Maior número\n'
          '  [ 4 ]- Novos números\n'
          '  [ 5 ]- Sair do programa')
    print(' ')
    n0 = int(input('Sua escolha: '))  # Opção escolhida
    print('-=' * 15)
    sleep(1)

    if n0 == 1:
        print('A soma dos numeros escolhido é: ')
        print('{} + {} = {}'.format(n1, n2, n1 + n2))  # Soma(opção 1)

    if n0 == 2:
        print('A multiplicação do números é:  ')
        print('{} x {} = {}'.format(n1, n2, n1 * n2))  # Multiplicação(opção 2)

    if n0 == 3:
        if n1 > n2:
            print('{} é maior que o número {}'.format(n1, n2))  # Primeiro número maior
        elif n2 > n1:
            print('{} é maior que o número {}'.format(n2, n1))  # Segundo número maior

    if n0 == 4:
        print('Digite novos números: ')  # Escolha de novos números
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))

    if n0 == 5:
        print('Obrigado pela participação! :)')  # FIM !
