num = [2 , 5 , 9 , 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2 , 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print('-=' *30)

'''[2, 5, 9, 1]
[2, 5, 3, 1]
[2, 5, 3, 1, 7]
[7, 5, 3, 2, 1]
[7, 5, 0, 3, 2, 1]
Essa lista tem 6 elementos.'''

num = [2 , 5 , 9 , 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2 , 0)
num.pop()
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

'''[2, 5, 9, 1]
[2, 5, 3, 1]
[2, 5, 3, 1, 7]
[7, 5, 3, 2, 1]
[7, 5, 0, 3, 2]'''

