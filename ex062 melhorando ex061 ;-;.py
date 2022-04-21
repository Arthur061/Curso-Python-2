print('')
print('Gerador de PA')
print('')

primeiro_termo = int(input('Primeiro termo: '))  # Perguntando 1° termo
razao = int(input('Razão: '))  # Primeira razão
termo = primeiro_termo  # Termo recebe primeiro_termo
contador = 1  # Contador começando com 1, começando contagem por 1
total = 0  # Total ainda é 0, calcular total quando progama finalizar
mais = 10  # Maximo que vai ganhar a mais do primeiro ao ultimo termo

while mais != 0:  # Executar enquanto mais for diferente de 0
    total += mais  # Total recebe o valor dele mesmo + o valor do mais
    while contador <= total:  # Enquanto contador for menor ou igual total, o comando vai executar
        print('{} ->'.format(termo), end='')  # Capricho
        termo += razao
        contador += 1

    print('PAUSA')
    mais = int(input('Quantos termos voce quer adiconar? '))

print('Progesso final terminou com {} termos'.format(total))