#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
resposta = False
cont = 0
while resposta != True:
    numero = randint(0, 10)
    cont += 1
    print('{:=^70}'.format (' JOGO DE ADIVINHA '))
    usuario = int(input("Tente adivinhar o número que o COMPUTADOR pensou (entre 0 e 10): "))
    print('=' *70)
    print('PROCESSANDO...')
    sleep(1)
    if usuario == numero:
        resposta = True
        print('Parabéns! Você \033[1;32mGANHOU!\033[m Você acertou depois de {} tentativas!!!'.format(cont))
    else:
        print('Que pena! Você \033[1;31mPEDEU!\033[m O número era {} e não {}! Tente novamente!!!'.format(numero, usuario))

