peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
# (altura ** 2) É a altura ao quadrado
imc = peso / (altura ** 2)
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('PARABENS,voce esta dentro do peso normal')
elif 25 <= imc < 30:
    print('ACIMA DO PESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE')
elif imc >= 40:
    print('Voce esta em OBESIDADE MÓRBIDA')