cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:7].upper() == 'MARINGÁ')

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))