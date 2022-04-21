primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é {} e ele é maior que o segundo valor'.format(primeiro_valor))
elif primeiro_valor < segundo_valor:
    print('O segundo valor é {} e ele é maior que o primeiro valor'.format(segundo_valor))
elif primeiro_valor == segundo_valor:
    print('Os dois valores são iguais!! :)')
