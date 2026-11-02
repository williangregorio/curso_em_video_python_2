'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('{:=^30}'. format (' PROGRESSÃO ARITIMÉTICA '))
print('{:^30}'. format ('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro = int(input('Digite o Primeiro Termo: '))
razao = int (input('Digite a Razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{}'.format(termo), end=' → ')
    termo += razao
    cont += 1
print('Acabou!')