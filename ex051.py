'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
print('{:=^30}'. format (' PROGRESSÃO ARITIMÉTICA '))
print('{:^30}'. format ('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro = int(input('Digite o Primeiro Termo: '))
razao = int (input('Digite a Razão: '))
decimo = primeiro + (10-1) * razao
for i in range (primeiro, decimo + razao, razao):
    print('{}'. format (i), end = ' -> ')
print('Acabou!')
