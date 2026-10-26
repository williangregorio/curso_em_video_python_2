'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
ano_atual = date.today().year
tot_menor = 0
tot_maior = 0
for pessoa in range (1, 8):
    nascimento = int(input('Qual o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = ano_atual - nascimento
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('A quantidade de maiores de idade são: {}'.format(tot_maior))
print('E a quantidade de menores de idade são: {}'.format(tot_menor))
