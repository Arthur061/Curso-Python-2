media1 = float(input('Digite sua primeira nota: '))
media2 = float(input('Digite sua segunda nota: '))

soma_media = (media1 + media2) / 2
print('Sua média foi de {}'.format(soma_media))

if soma_media < 5:
    print('Sua média foi menor que 5!! :(')
    print('Voce está reprovado :(')

elif soma_media >= 5 and soma_media < 7:
    print('Uma "boa" média, mas ela não é o suficiente.')
    print('Voce está de recuperação!!')

elif soma_media >= 7:
    print('Parabens!!! :)')
    print('Voce teve boas notas e boas média, voce está aprovado')
