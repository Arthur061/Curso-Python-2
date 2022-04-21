print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

numero_termos = int(input('Quantos termos voce quer ver? '))  # Termos de entrada ( quantidade)

t1 = 0
t2 = 1
contador = 3
print('{} -> {} '.format(t1, t2), end='')  # Imprime t1 e t2 (0, 1)

while contador <= numero_termos:
    t3 = t1 + t2  # Cria t3 dentro do loop ja somando t1 + t2
    print('-> {}'.format(t3), end='')  # Imprime t3 já com o valor atual do loop
    t1 = t2  # Valor dependendo do loop
    t2 = t3  # Valor dependendo do loop
    contador += 1  # Sempe que o loop ocorrer vai adicionar 1

print('-> FIM')