'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

print(f'{' CADASTRO DE PESSOAS ':=^30}')
maiores = homens = mulheres = 0
while True:
    opção = sexo = ' '
    idade = int(input('Qual a idade? '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('Pessoa cadastrada com Sucesso!')
    while opção not in 'SN':
        opção = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        print('FIM DO PROGRAMA!')
        break
print (f'{' Resultados ':=^30}')
print (f'Pessoas com mais de 18 anos = {maiores}')
print (f'Homens = {homens}')
print (f'Mulheres abaixo de 20 anos = {mulheres}')