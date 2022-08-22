def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {largura}x{comprimento} é de {a}m².')


l = float(input('LARGURA: (m)'))
c = float(input('COMPRIMENTO: (m)'))
area(l, c)