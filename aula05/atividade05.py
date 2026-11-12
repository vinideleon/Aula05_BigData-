#crie um algoritmo, que solicite ao usuario a digitação de um numero(inteiro ou decimal). o algoritmo entao, deve exibir uma mensagem indicando, se o numero é:

numero = float(input('informe um numero: ' ))

match numero:
    case numero if numero > 0:
        print(f'{numero} é positivo')
    case numero if numero < 0:
        print(f'{numero} é negativo')
    case 0:
        print('zero')
    

