valor_casa = float(input('Qual o valor da casa desejada ? R$'))
salario = float(input('Qual o seu salario mensal ? R$'))
pagamento_total = int(input('Em quantos anos voce pretende pagar a casa ? '))

prestação = valor_casa / (pagamento_total * 12)

mensalidade = salario * 30 / 100

if prestação <= mensalidade:
    print('Emprestimo foi aceito!!')
    print('Valor a pagar mensalmente: R${:.2f}'.format(mensalidade))
else:
    print('Emprestimo foi negado!!')
    print('Infelizmente o preço da casa e alto demais, mesmo pagando em {} anos, a prestação da casa vai dar mais de 30% do seu salario'.format(pagamento_total))