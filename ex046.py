#Primeiro termo e a razao de uma PA, mostrando apenas os 10 primeiros

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro , decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')