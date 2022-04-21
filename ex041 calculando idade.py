from datetime import date

nascimento = int(input('Em qual ano voce nasceu ? '))
ano_atual = date.today().year

idade = ano_atual - nascimento

if idade <= 9:
    print('Voce tem {} anos e portanto sua categoria na natação será MIRIM.'.format(idade))
elif idade > 9 and idade <=14:
    print('Voce tem {} anos e portanto sua categoria na natação será INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Voce tem {} anos e portanto sua categoria na natação será JUNIOR'.format(idade))
elif idade == 20:
    print('Voce tem {} anos e portanto sua categoria na natação será SÊNIOR'.format(idade))
else:
    print('Voce tem {} anos e portanto sua categoria na natação será MASTER'.format(idade))
