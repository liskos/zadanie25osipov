file = open(file='Задание 24/24.txt')
k = 0
for s in file:
    for a in 'ABCDEFGHIJKLMNOPRQSTUWYXWZ':
        l = 'Z' + a + 'RO'
        if l in s:
            k += 1
            break
print(k)
