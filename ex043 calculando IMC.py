peso = float(input('Quanto você pesa em KG ? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / (altura ** 2)

print('Seu IMC é de: {:.1f}'.format(imc))

if imc < 18.5:
    print('De acordo com o seu IMC, voce está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('De acordo com o seu IMC, voce está com o peso ideal')
elif imc >= 25 and imc <= 30:
    print('De acordo com o seu IMC, voce está em sobrepeso')
elif imc >= 30 and imc <= 40:
    print('De acordo com o seu IMC, voce está em obesidade')
elif imc > 40:
    print('De acordo com o seu IMC, voce está com obesidade morbida')