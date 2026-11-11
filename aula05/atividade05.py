#crie um algoritmo, que solicite ao usuario a digitação de um numero(inteiro ou decimal). o algoritmo entao, deve exibir uma mensagem indicando, se o numero é:

print ('''
positivo = 1 a 9
negativo = -1 a -9
zero = 0

''')

numero = int(input('escolha um numero de 1 a 9: ' ))

match numero:
    case opcao if 1 <= numero <= 9:
        print('positivo')
    case opcao if -1 >= numero >= -9:
        print('negativo')
    case 0:
        print('zero')
    

