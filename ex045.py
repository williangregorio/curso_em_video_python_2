#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('{:=^40}'.format(' Jogo do Jokenpô '))
jogador = int(input('''Escolha uma das opções abaixo:
[1] PEDRA
[2] PAPEL
[3] TESOURA
opção: '''))
print('=' * 100)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('=' * 100)
opção = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
if jogador >= 1 and jogador <=3:
  computador = randint(1, 3)
  if jogador == computador:
    print('Você escolheu {} e o computador escolheu {}, sendo assim, houve \033[1;33mEMPATE\033[m!'.format(opção[jogador], opção[computador]))
  elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 3) or (jogador == 3 and computador == 1):
    print('Você escolheu {} e o computador escolheu {}, sendo assim, você \033[1;31mPERDEU\033[m!'.format(opção[jogador], opção[computador]))
  else:
    print('Você escolheu {} e o computador escolheu {}, sendo assim, você \033[1;32mGANHOU\033[m!'.format(opção[jogador], opção[computador]))
else:
  print('Opção selecionada inválida, tente novamente!!!')