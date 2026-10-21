'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
if primeiro_numero > segundo_numero:
    print('O PRIMEIRO número é maior do que o segundo!')
elif primeiro_numero < segundo_numero:
    print('O SEGUNDO número é maior do que o primeiro!')
else:
    print('O números são iguais!')
