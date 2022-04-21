from datetime import date
ano = int(input('Qual o ano que voce nasceu? '))
atual = date.today().year

idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print('Ainda não chegou sua hora de se alistar, voce tem (ou vai fazer) {} anos e faltam {} ano(s) para seu alistamento'
          .format(idade, saldo))
    ano_alistamento = atual + saldo
    print('Seu alistamento sera no ano de {}'.format(ano_alistamento))
elif idade == 18:
    print('Voce tem que se alistar imediatamente, esse ano voce faz (ou já fez) 18 anos!')
elif idade > 18:
    saldo = idade - 18
    print('Já passou seu tempo de alistamento, voce tem {} anos e se alistou a {} anos atrás'
          .format(idade, saldo))
    ano_alistamento = atual - saldo
    print('Seu alistamento foi no ano de {}'.format(ano_alistamento))