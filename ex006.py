n1 = int(input('Digite um numero : '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
raizQ = pow(n1,(1/2))
# raiz quadrada pode ser calculada pela função pow(n1,(1/2)
# a raiz quadrada pode ser representado pela exponenciação , aonde n1 (**elevado) (1/2)
print('O dobro de {} é {}'.format(n1,dobro))
print('O triplo de {} é {}'.format(n1,triplo))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n1,raiz))
print('A raiz quadrada de {} usada pela função {:.2f}'.format(n1,raizQ))