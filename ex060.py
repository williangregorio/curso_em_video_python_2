'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

# Resolvendo da forma convencional
nun = int(input('Digite um número para ver seu fatorial: '))
cont = nun
fatorial = 1
print('Calculando {}! ==> '.format(nun),end='')
while cont > 0:
    print(' {} '. format(cont),end='')
    if cont > 1:
        print('x',end='')
    else:
        print('=', end='')
    fatorial *= cont
    cont -= 1
print(' {}'.format(fatorial))

'''# Usando módulo
from math import factorial
nun = int(input('Digite um número para ver seu fatorial: '))
fac = factorial(nun)
print('O fatorial de {}! é: {}'.format(nun, fac))'''
