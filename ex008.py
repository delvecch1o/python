medida = float(input('Uma distancia em metros: '))

cm = medida * 100
mm = medida * 1000

km = medida / 1000
hectometro = medida / 100
decametro = medida / 10
decimetro = medida * 10



print('A medida em {}m corresponde a {}km e {}hectometro , {}decametro , {}decimetro '.format(medida, km, hectometro, decametro, decimetro))
print('A medida em {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))