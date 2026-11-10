#considerando as quatro notas obtidas por um estudante ao longo do periodo letivo, elabore um programa em python
#que calcule a media final e apresente a situação do estudante conforme os seguintes critérios:
#media igual ou superior a 7,0: aprovado/ media igual ou superior a 5,0 e inferior a 7,0: em recuperação
#media inferior a 5,0: reprovado

nota1 = float(input('qual é a sua nota n1?? '))
nota2 = float(input('qual é a sua nota n2?? '))
nota3 = float(input('qual é a sua nota n3?? '))
nota4 = float(input('qual é a sua nota n4?? '))

nota_total = (nota1 + nota2 + nota3 + nota4) / 4

if nota_total >= 7:
     print(f'Parabens sua nota é {nota_total} \nvocê está aprovado!')

elif nota_total >= 5:
    print(f'sua nota é {nota_total} \nvocê está em recuperação!')

else:
    print(f'sua nota é {nota_total} \nvocê está reprovado!')
    

