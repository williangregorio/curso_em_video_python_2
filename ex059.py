'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
nun1 = float(input('Digite o primeiro valor: '))
nun2 = float(input('Digite o segundo valor: '))
opcao = 0
print('Selecione uma das opções')
while opcao != 5:
    opcao = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nOpção: '))
    print ('-'*50)
    if opcao == 1:
        soma = nun1 + nun2
        print('A soma dos números {} + {} = {}'.format (nun1, nun2, soma))
    elif opcao == 2:
        multiplicacao = nun1 * nun2
        print('A multiplicação dos números {} x {} = {}'.format(nun1, nun2, multiplicacao))
    elif opcao == 3:
        if nun1 > nun2:
            maior = nun1
        else:
            maior = nun2
        print('Entre {} e {} o maior é {}'.format(nun1, nun2, maior))
    elif opcao == 4:
            nun1 = float(input('Digite o primeiro valor: '))
            nun2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
            print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente!')
    print('-' * 50)