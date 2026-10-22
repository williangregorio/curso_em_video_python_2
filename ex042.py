'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

r1 = float(input('Digite o comprimento da RETA 1:'))
r2 = float(input('Digite o comprimento da RETA 2:'))
r3 = float(input('Digite o comprimento da RETA 3:'))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 == r3:
        print('As retas podem formar um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('As retas podem formar um triângulo ESCALENO!')
    else:
        print('As retas podem formar um triângulo ISÓSCELES!')
else:
    print('As retas NÃO podem formar um triângulo!')
