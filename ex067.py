'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
print(f'{' TABUADAS ':=^70}')
while True:
    num = int(input('Qual o número que deseja ver a tabuada? [negativo finaliza] '))
    print('=' * 70)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('=' * 70)
print('Finalizamos! Volte sempre')