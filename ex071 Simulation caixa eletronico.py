print('=' * 30)
print('{:^30}'.format('BANCO ART'))
print('=' * 30)

valor = int(input('Digite o valor de saque: R$ '))  # Recebe valor
total = valor
contagem_cedulas = 0
cedulas = 50


while True:
    if total >= cedulas:  # Se o valor(total) for maior que o valor das cedulas
        total -= cedulas
        contagem_cedulas += 1

    else:
        if contagem_cedulas > 0:
            print(f'Foi usado {contagem_cedulas} notas de R${cedulas}')  # Imprime result de quantas notas foi usada

            if cedulas == 50:
                cedulas = 20

            elif cedulas == 20:
                cedulas = 10

            elif cedulas == 10:
                cedulas = 1
            contagem_cedulas = 0

            if total == 0:
                break


print('=' * 30)
print('{:^30}'.format('Obrigado !! Volte sempre ao BANCO ART'))
print('=' * 30)