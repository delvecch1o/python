def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n .isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro.\033[m')
        if ok:
            break
    return valor

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'CUIDADO'
    else:
        r['situacao'] = 'RUIN'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)

n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
