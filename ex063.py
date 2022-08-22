def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores ..')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao total.')
    print(f'O maior valor informado foi {maior}')



maior(2, 9, 4, 5, 6, 7, 4, 2)
maior(4, 7, 0)
maior(1, 2, 3)
maior(6)
maior()