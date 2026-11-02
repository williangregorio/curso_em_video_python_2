#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
resposta = False
cont = 0
numero = randint(0, 10)
print('{:=^70}'.format (' JOGO DE ADIVINHA '))
print('Vamos jogar? Tente adivinhar o número que pensei (entre 0 e 10)')
while resposta != True:
    cont += 1
    usuario = int(input('Palpite: '))
    print('PROCESSANDO',end='')
    for i in range (1, 10):
        sleep(0.2)
        print('.',end='')
    if usuario == numero:
        resposta = True
        print('\nParabéns! Você \033[1;32mGANHOU!\033[m Você acertou depois de {} tentativas!!!'.format(cont))
    else:
        if usuario > numero:
            print('\nNão foi dessa vez! Tente um número mais baixo!')
        elif usuario < numero:
            print('\nNão foi dessa vez! Tente um número mais alto!')
