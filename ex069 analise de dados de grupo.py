print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)

contador_idade = total_homem = mulher_idade = 0

while True:
    print('-' * 20)
    idade = int(input('Idade: '))  # Ler idade
    sexo = str(input('Sexo [M / F]: ')).upper().strip()[0]  # Ler sexo

    while sexo not in 'FM':
        sexo = str(input('Sexo [M / F]: ')).upper().strip()[0]
    print('-' * 20)
    continuar = str(input('Quer continuar? [S / N] ')).upper().strip()[0]  # Caso queira continuar

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S / N] ')).upper().strip()[0]

    if idade > 18:  # Quantas pessoas são maiores de 18
        contador_idade += 1

    if sexo == 'M':  # Quantas pessoas são homens
        total_homem += 1

    if sexo == 'F':
        if idade < 20:  # Quantas mulheres tem menos de 20 anos
            mulher_idade += 1

    if continuar == 'N':
        break


print('Programa finalizado !')
print('')
print(f'Total de pessoas com mais de 18 anos é {contador_idade}')
print(f'Ao todo temos {total_homem} homens cadastrados')
print(f'E temos um total de {mulher_idade} mulheres com menos de 20 anos.')
