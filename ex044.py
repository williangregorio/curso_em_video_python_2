'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Digite o valor do produto R$: '))
opção = int(input('''Qual seria a forma de pagamento?
[1] À vista no dinheiro
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Opção: '''))
if opção == 1:
    total = preço - (preço * 10/100)
    print('O produto que custa R${:.2f}, com pagamento à vista em dinheiro vai para R${:.2f}'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5/100)
    print('O produto que custa R${:.2f}, com pagamento à vista no cartão vai para R${:.2f}'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('O produto que custa R${:.2f}, com pagamento em 2x no cartão fica em R${:.2f} com parcelas de R${:.2f}'.format(preço, total, parcela))
elif opção == 4:
    qtd_parcelas = int(input('Qual a quantidade de parcelas? '))
    total = preço + (preço * 20/100)
    parcela = total / qtd_parcelas
    print('O produto que custa R${:.2f}, com pagamento em {}x no cartão vai para R${:.2f} e o valor das parcelas serão de R${:.2f}'.format(preço, qtd_parcelas, total, parcela))
else:
    print('Opção escolhida não é válida!')