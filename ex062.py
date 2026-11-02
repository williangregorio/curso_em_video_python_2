'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('{:=^30}'. format (' PROGRESSÃO ARITIMÉTICA '))
print('{:^30}'. format ('10 TERMOS DE UMA PA'))
print('=' * 30)
primeiro = int(input('Digite o Primeiro Termo: '))
razao = int (input('Digite a Razão: '))
cont = 1
termo = primeiro
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' → ')
        termo += razao
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos a mais deseja mostrar? '))
print('Progressão finalizada com um total de {} termos'. format(total))

