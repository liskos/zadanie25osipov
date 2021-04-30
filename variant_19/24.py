file = open(file='24-s1.txt')
k = 0
for s in file:
    for i in 'ABCDEFGHIJKLMNOPQRSTUVYXWZ':
        r = 'A' + i + 'R'
        if r in s:
            k += 1
            break
print(k)
