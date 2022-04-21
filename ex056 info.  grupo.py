soma_idade = 0  # Soma das idades
media_idade = 0  # Calculando média das idades, após a soma
maioridade_homem = 0  # Definindo homem mais velho
nome_velho = ''  # Nome do homem mais velho
total_mulher20 = 0  # Total de mulhers com menos de 20 anos

# Calculando média de idades
for info in range(1, 5):
    print('     {}° PESSOA     '.format(info))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F / M): ')).strip()
    soma_idade += idade

    # Calculando nome e idade do homem mais velho
    if info == 1 or info == 2 or info == 3 or info == 4 and sexo in 'Mm':
        maioridade_homem = idade
        nome_velho = nome
    if sexo == 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome

            # Calculo das mulheres + novas
    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1

media_idade = soma_idade / 4

print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher20))

