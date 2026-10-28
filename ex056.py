'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
# a média de idade do grupo, 
# qual é o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.'''

cont_mulheres = 0
maior_idade = 0
homem_velho = ''
soma_idade = 0

for p in range(1, 5):
    print('===== Dados da {}ª Pessoa ====='.format(p))

    nome = str(input('Qual o nome: ')).upper().strip()
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo\n[M] Masculino\n[F] Feminino\nOpção: ')).upper().strip()

    print('=' * 30)

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            homem_velho = nome

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

media_idade = soma_idade / 4

print('A soma de todas as idades é:', soma_idade)
print('A média de idade do grupo é: {:.1f}'.format(media_idade))
print('O homem mais velho é:', homem_velho)
print('Tivemos {} mulheres abaixo de 20 anos na pesquisa'.format(cont_mulheres))
