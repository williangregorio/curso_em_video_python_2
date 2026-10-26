'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
texto = str(input('Digite uma frase: ')).strip().upper()
texto_junto = texto.replace(' ', '')
texto_invertido = ''
#Opção sem uso do FOR
#texto_invertido = texto_junto[::-1]
for i in range(len(texto_junto)-1, -1, -1):
    texto_invertido += texto_junto[i]
print('O texto invertido ao que digitou é: {}'.format(texto_invertido))
if texto_junto == texto_invertido:
    print('Existe Palíndromo!')
else:
    print('Não existe Palíndromo!')
