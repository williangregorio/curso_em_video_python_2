'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
nun = cont = soma =0
while nun != 999:
    nun = int(input('Digite um número (999 sair do programa): '))
    if nun != 999:
        cont += 1
        soma += nun
print('Foram digitados {} números e a soma deles é de {}'.format(cont, soma))
