'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
vitorias = total = 0
print(f'{' Jogo do Par ou Ímpar ':=^50}')
while True:
    jogador = int(input('Digite um número de 0 a 10: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = resultado = ' '
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o Computador jogou {computador}. O resultado é {total} que é {resultado}')
    if tipo == 'P':
        if total %2 == 0:
            print('Você VENCEU!!')
            vitorias += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você VENCEU!!')
            vitorias += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente!')
    print('=' * 50)
print('=' * 50)
print(f'GAME OVER! Você ganhou {vitorias} vezes')
print('=' * 50)