'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
numero = int(input('Digite um número: '))
cont = 0
for i in range (1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format (i), end=' \033[m')
print('\nO número {} é divisível {}X!'.format (numero, cont))
if cont == 2:
    print('Sendo assim, {} é PRIMO!'.format(numero))
else:
    print('Sendo assim, {} NÃO é PRIMO!'.format(numero))