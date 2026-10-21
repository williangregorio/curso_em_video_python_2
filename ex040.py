'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5.0:
    print('Que pena, sua média foi {:.2f} - Você foi REPROVADO!'.format(média))
elif média > 5.0 and média < 6.9:
    print('Quase lá, sua média foi {:.2f} - Você está de RECUPERAÇÃO!'.format(média))
else:
    print('Que ótimo, sua média foi {:.2f} - Você está APROVADO!'.format(média))
