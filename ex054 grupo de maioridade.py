from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0

for pessoas in range(1, 8):
    nascimento = int(input('Em qual ano a {}° pessoa nasceu ? '.format(pessoas)))
    idade = atual - nascimento

    if idade >= 21:
        total_maior += 1

    else:
        total_menor += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(total_maior))
print('E tambem tivemos ao todo {} pessoas menores de idade.'.format(total_menor))