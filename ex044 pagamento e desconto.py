preço_produto = float(input('Qual o preço do produto ? '))

print('Escolha uma das opções abaixo para efetuar o pagamento: ')
print('[ 1 ]- Á vista dinheiro/cheque \n'
      '[ 2 ]- Á vista no cartão \n'
      '[ 3 ]- Em até 2x no cartão \n'
      '[ 4 ]- 3x ou mais no cartão')

escolha = int(input())

if escolha == 1:
    print('Voce escolheu pagamento á vista/cheque e vai ganha desconto de 10%')
    total_dinheiro = preço_produto - (preço_produto * 10 / 100)
    print('Total a pagar será R${:.2f}'.format(total_dinheiro))

elif escolha == 2:
    print('Voce escolheu pagamento no cartão e ganhou desconto de 5%')
    total_cartao = preço_produto - (preço_produto * 5 / 100)
    print('Total a pagar será R${:.2f}'.format(total_cartao))

elif escolha == 3:
    print('Voce escolheu pagar 2x no cartão e então o preço não será alterado')
    dividido2x = preço_produto / 2
    print('Total a pagar será 2x de R${:.2f}'.format(dividido2x))

elif escolha == 4:
    print('Voce escolheu pagar em 3x ou mais então pagará 20% de juros')
    quantidade_parcelas = int(input('Quantas parcelas ? '))
    total_juros = preço_produto + (preço_produto * 20 / 100)
    mensalidade = total_juros / quantidade_parcelas
    print('Total a pagar será R${:.2f} em {}x de {:.2f}'.format(total_juros, quantidade_parcelas, mensalidade))
else:
    print('Opção inválida. Tente novamente :(')