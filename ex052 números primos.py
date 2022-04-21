num = int(input('Digite um número: ')) # Pegunta o número para o usúario.
total = 0
for c in range(1, num + 1):  # Comando usado para fazer a contagem do número.
    if num % c == 0:  # Se o restante da divisão for igual a 0.
        print('\033[34m', end=' ')  # Por quais números foi divisivel.
        total += 1
    else:
        print('\033[31m', end=' ')  # Por quais números não foi divisivel.
    print('{}'.format(c), end=' ')  # Imprime os número já com as config a cima.
print('\n \033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele É PRIMO !!')  # Se o número só foi divisivel por dois número (1 e ele mesmo)
else:
    print('E por isso ele NÃO É PRIMO')  # Se o número foi divisivel por mais de 2 números
