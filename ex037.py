'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
numero = int(input('Digite um número inteiro qualquer: '))
base_conversao = int(input('''Digite qual a base de conversão deseja
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
sua opção: ''').strip())
if base_conversao == 1:
    print('O número {} em base BINÁRIA = {}'.format(numero,bin(numero)[2:]))
elif base_conversao == 2:
    print('O número {} em base OCTAL = {}'.format(numero, oct(numero)[2:]))
elif base_conversao == 3:
    print('O número {} em base HEXADECIMAL = {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('A opção escolhida {} não tem conversão!'.format(base_conversao))
