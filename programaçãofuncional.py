n = [1,2,3,4,5]

quadrados = list(map(lambda x: x**2, list(filter(lambda x: x % 2 == 0, n))))

print(quadrados)

#programação funcional