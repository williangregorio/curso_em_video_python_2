'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
print('{:=^60}'.format (' TABUADA '))
numero = int(input('Digite qual número deseja a tabuada = '))
for i in range (1, 11):
    print('{} x {:2} = {}'.format (numero, i, (numero * i)))
print('='* 60)
