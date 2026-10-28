peso_menor = 0
peso_maior = 0
for cont in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(cont)))
    if cont == 1:
        peso_menor = peso
        peso_maior = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
        
print('O menor peso digitado foi: {:.1f}kg'.format(peso_menor))
print('O maior peso digitado foi: {:.1f}kg'.format(peso_maior))    
