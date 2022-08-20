nota1 = float(input('Informe a Primeira nota: '))
nota2 = float(input('Informe a Segunda nota: '))
media = (nota1 + nota2) / 2
print('A media do Aluno foi {}'.format(media))
if 7 > media >= 5 :
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')