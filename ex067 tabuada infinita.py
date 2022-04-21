while True:
    numero = int(input('Digite um número para saber sua tabuada: '))  # Ler número

    if numero < 0:  # Se o número for menor que 0 o progama vai acabar
        break

    for n in range(1, 11):  # Tabuada 1 a 10
        print(f'{numero} x {n} = {numero * n}')

print('PROGAMA DE TABUADA CHEGOU AO FIM!! Volte sempre')