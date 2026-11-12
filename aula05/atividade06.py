#escreva um algoritmo em python, que receba um valor monetario de venda fornecido pelo usuario e classifique esta venda de acordo com as seguintes regras:
#venda pequena: valores inferiores a 100; venda media: valores entre 100(inclusivo) e 500(exclusivo); venda grande: valores iguais ou superiores a 500.abs

print('''
venda pequena: inferior a 100.
venda media:  100 a 500
venda grande:  500

''')

venda = int(input('escolha o valor da venda: '))

match venda:
    case venda if venda < 100:
        print('venda pequena')
    case venda if venda < 500:
        print('venda media')
    case venda if venda > 500:
        print('venda grande')
