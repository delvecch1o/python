def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido.')
            continue
        else:
            return n

num = leiaInt('Digite um valor: ')
print(f'O valor difitado foi {num}')
