'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date

ano_atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - nascimento
if idade <= 9:
    print('Quem nasceu em {}, hoje em {} possui {} anos de idade e está na categoria MIRIM de natação'
          ''.format(nascimento, ano_atual, idade))
elif idade <= 14:
    print('Quem nasceu em {}, hoje em {} possui {} anos de idade e está na categoria INFANTIL de natação'
          ''.format(nascimento, ano_atual, idade))
elif idade <= 19:
    print('Quem nasceu em {}, hoje em {} possui {} anos de idade e está na categoria JÚNIOR de natação'
          ''.format(nascimento, ano_atual, idade))
elif idade <= 25:
    print('Quem nasceu em {}, hoje em {} possui {} anos de idade e está na categoria SÉNIOR de natação'
          ''.format(nascimento, ano_atual, idade))
else:
    print('Quem nasceu em {}, hoje em {} possui {} anos de idade e está na categoria MASTER de natação'
          ''.format(nascimento, ano_atual, idade))
