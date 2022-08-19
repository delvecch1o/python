salario = float(input('Qual é o seu salario? R$'))
novo = salario + (salario * 15 / 100)
print('O seu salario atual é R${:.2f} , com 15% de aumento R${:.2f}'.format(salario, novo))