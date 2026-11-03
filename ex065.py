'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
cont = media = soma = maior = menor = 0
continuar = ''
num = int(input('Digite um valor qualquer: '))
maior = menor = num
while continuar != 'N':
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    soma += num
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'S':
        num = int(input('Digite um valor qualquer: '))
media = soma / cont
print('Foram digitados {} valores. A média entre eles foi {:.2f}, o maior foi {} e o menor foi {}'.format(cont, media, maior, menor))