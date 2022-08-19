import random
print('Quem vai Pagar a conta entre os 4')
n1 = str(input('Primeiro: '))
n2 = str(input('Segundo : '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto : '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))