#uma empresa utiliza codigos numericos para identificar os setores de seus funcionarios. crie um algoritmo que solicite em codigo ao usuario e informe o setor
#correspondente. considere que 1 corresponde ao marketing; 2 ao financeiro;3 a 5 administração; 6 a 9 TI; 10 a 20 serviços gerais. 
# valores fora dessa opçãoes devem ser consideradas invalidas

# Estrutura Match Case
print('''
[1] - Marketing
[2] - Financeiro
[3 a 5] - Administração
[6 a 9] - TI
[10 a 20] - Serviços gerais
''')

opcao = int(input('escolha uma opção: '))

match opcao:
    case 1:
        print('marketing')
    
    case 2:
        print('Financeiro')
    
    case 3 | 4 | 5:
        print('Administração')
    
    case opcao if 6 <= opcao <= 9:
        print('TI')

    case opcao if 10 <= opcao <= 20:
        print('Serviços Gerais')
    
    case _:
        print('Opção invalida! ')

