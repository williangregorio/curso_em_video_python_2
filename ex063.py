'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('='* 50)
print('Sequencia de Fibonacci')
print('='* 50)
quantidade = int(input('Qual a quantidade de elementos quer visualizar? '))
anterior = 0
atual = 1
cont = 0
proximo = 0
while cont < quantidade:
    print('{}'.format(anterior),end=' - ')
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    cont += 1
print('FIM')