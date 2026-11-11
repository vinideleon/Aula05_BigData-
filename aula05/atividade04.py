#escreva um programa, que leio o codigo de origem de um produto e imprima na tela a regiao de sua procedencia, conforme a tabela abaixo:
#codigo 1 - sul; codigo 2 - norte; codigo 3 - leste; codigo 4 - oeste; codigo 5 ou 6 nordeste; codigo 7 a 9 sudeste; codigo 10 centro oeste; codigo 11 noroeste;
#caso o codigo não seja nenhum dos especificados, o produto deve ser encarado como "importado".

print('''
[1] - Sul
[2] - Norte
[3] - leste
[4] - oeste
[5 ou 6] - nordeste
[7 a 9] - sudeste
[10] - centro oeste
[11] - noroeste
''')

codigo = int(input('escolha um codigo: '))

match codigo:
    case 1:
        print('sul')
    
    case 2:
        print('Norte')
    
    case 3:
        print('leste')
    
    case 4:
        print('oeste')
    
    case 5 | 6:
        print('nordeste')
    
    case opcao if 7 <= codigo <= 9:
        print('sudeste')
    
    case 10:
        print('centro-oeste')
    
    case 11:
        print('Noroeste')
    
    case _:
        print('importado')