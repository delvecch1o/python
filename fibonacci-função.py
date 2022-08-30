#sequencia fibonacci: 0 1 1 2 3 5 8 13 21 34 55 89 ...
            #posiçao:   1 2 3 4 5 6  7  8  9 10 11

def fibonacci(posicao):
    if posicao <= 1:
        return posicao
    else:
        return fibonacci(posicao - 1) + fibonacci (posicao - 2)
a = int(input('Digite a Posicao: '))
res = fibonacci(a)
print('Na %d Posição o valor Fibonnaci é: %d ' %(a, res))