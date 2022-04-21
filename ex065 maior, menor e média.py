continua = 'S' 'N'
soma = média = contagem = maior = menor = 0


while continua not in 'N':
    print('-' * 30)
    número = int(input('Digite um número: '))
    continua = str(input('Quer continuar? [S / N] ')).strip().upper()[0]
    print('-' * 30)
    contagem += 1
    soma += número
    média = soma / contagem

    if continua == 'N':
        soma += número

    if contagem == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número

print('~' * 30)
print('Voce digitou {} números e sua média foi {:.2f}'.format(contagem, média))
print('O maior número foi {} e o menor número foi {}'.format(maior, menor))
print('~' * 30)
