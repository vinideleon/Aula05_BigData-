#uma escola concede uma bolsa de estudos para alunos que atendem a dois criterios ao mesm tempo: Nota final maior ou igual a 7,0; freq maior ou = a 75%
#o programa deve calcular o valor da bolsa:20% da mensalidade. escreva um programa em python que leia a nota final, a frequencia e o valor da mensalidade
# se o aluno tiver nota maior ou igual a 7 e frequencia maior ou igual a 75%, calcule e mostre o valor da bolsa. caso contrario, informe que ele n tem direito.

nota = float(input('informe a sua nota final? '))
frequencia = int(input('informe a sua frequencia? '))
mensalidade = float(input('qual é o valor da sua mensalidade? '))

if nota >= 7 and frequencia >= 75:
    bolsa = (0.20 * mensalidade) 
    print(f'Parabens você atendeu a todos os requisitos e sua bolsa foi aprovada e você recebeu um desconto de 20%. \n o valor da sua bolsa é: {bolsa}') 

else:
    print(f'você não tem direito a bolsa! melhore seu rendimento.')
   


