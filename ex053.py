palavras = ('bom', 'dia', 'hoje', 'está', 'um', 'otimo', 'dia', 'para', 'dormir', 'levando', 'em', 'conta', 'que', 'é', 'domingo')



for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáeéioóu':
            print(letra, end=' ')