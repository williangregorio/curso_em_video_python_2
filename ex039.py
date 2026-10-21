'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual- nascimento
print('Quem nasceu em {} tem {} anos de idade em {}'.format(nascimento, idade, ano_atual))

if idade < 18:
    print('Você ainda irá se alistar ao serviço militar, faltam {} anos para isso!'.format(18 - idade))
elif idade == 18:
    print('Você está no momento exato de se alistar no serviço militar')
else:
    print('Você já ultrapassou o período de alistamento em {} anos!'.format(idade - 18))

