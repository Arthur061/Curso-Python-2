número_interio = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Para Binario')
print('[ 2 ] Para Octal')
print('[ 3 ] Para Hexadecimal')
x = int(input(''))

if x == 1:
    print('{} convertdio para BINARIO é igual a {}'.format(número_interio, bin(número_interio)[2:]))

elif x == 2:
    print('{} convertdio para OCTAL é igual a {}'.format(número_interio, oct(número_interio)[2:]))

elif x == 3:
    print('{} convertdio para HEXADECIMAL é igual a {}'.format(número_interio, hex(número_interio)[2:]))

else:
    print('Opção invalida!! Tente novamente :(')