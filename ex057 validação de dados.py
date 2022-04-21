sexo = str(input('Digite seu sexo: [M / F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Opção incorreta, digite novamente: ')).strip().upper()[0]

if sexo == 'M':
    print('Voce é do sexo masculino')

elif sexo == 'F':
    print('Voce é do sexo feminino')