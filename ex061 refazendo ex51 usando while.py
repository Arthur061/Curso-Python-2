print('')
print('=~' * 10)
print('GERADOR DE PA')
print('=~' * 10)
print('')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1

print('FIM')