distancia = float(input('Qual é a distancia da sua viagem?'))
print('Voce esta preste a comecar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem sera de R${:.2f}'.format(preco))