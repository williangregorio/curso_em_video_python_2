'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado.'''

valor_casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual é o valor do seu salário? R$ '))
qtd_anos = int(input('Em quantos anos deseja pagar seu financiamento imobiliário? '))
prestacao = float(valor_casa / (qtd_anos * 12))
print('Valor da casa escolhida:\033[1:32m R${:.2f}\33[m'.format(valor_casa))
print('Valor do salário do comprador:\33[1:32m R${:.2f}\33[m'.format(salario))
print('Quantidade de anos para pagar o imóvel:\33[1:32m {}\33[m'.format(qtd_anos))
print('O valor da prestação:\33[1:32m R${:.2f}\33[m'.format(prestacao))
if prestacao >= (salario * 30 / 100):
    print('Sua compra foi \33[1:31mNEGADA\33[m pois excede o limite de 30% de seu salário!')
else:
    print('Sua compra foi \33[1:32mAPROVADA\33[m! Curta sua nova casa!')

