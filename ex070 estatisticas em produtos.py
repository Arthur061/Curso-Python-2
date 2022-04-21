print('-' * 30)
print(' LOJINHA DO SEU ZÉ ')
print('-' * 30)

total = total_valores = menor_valor = contador = 0
nome_menor = ''

while True:
    print('')
    nome = str(input('Nome do produto: '))  # Recebe nome do produto
    valor = float(input('Valor do produto: R$'))  # Recebe valor do produto
    contador += 1
    print('')
    total += valor
    print('')
    print('')
    continuar = str(input('Quer continuar? [S / N] ')).upper().strip()[0]  # Pergunta se quer continuar

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
    print('')
    print('')

    if contador == 1:  # Definir  qual o menor preço e qual é o produto
        menor_valor = valor
        nome_menor = nome

    else:
        if valor < menor_valor:  # Definir, caso o outro seja False, qual o menor preço e produto
            menor_valor = valor
            nome_menor = nome

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S / N] ')).upper().strip()[0]

    if continuar == 'N':
        break

print('')
print('-------FIM DO PROGAMA-------')
print('')
print(f'O total da compra foi R${total}')
print(f'O total de produtos custando mais de R$1000.00 é de {total_valores} produtos')
print(f'O menor valor foi {nome_menor} que custa R${menor_valor}')