#uma loja da frete gratis se o cliente atender a pelo menos uma destas condições: compra acima de R$ 200,00; cliente é cadastrado no programa de fidelidade.
#se tiver direito ao frete gratis, o programa deve calcular o valor final da compra sem o frete. caso contrario, deve somar o frete de R$ 25,00
#ecreva em um programa em python que leia o valor da compra e pergunte se o cliente é cadastrado no programa de fidelidade.

compra = float(input('qual é o valor da sua compra? '))
programa_de_fidelidade = (input('você é cadastrado no programa de fidelidade? [S/N] ')).lower()[0]

#CONSTANTE ela não varia
FRETE = 25


if compra > 200 or programa_de_fidelidade == ('s'):
    frete = 0
    print(f'valor da sua compra é {compra}')

else:
    valor_final = compra + frete
    print(f'o frete fica no valor {frete}, o valor total da sua compra é {valor_final} ')

