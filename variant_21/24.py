file = open(file='Задание 24/24.txt')
k = 0
for st in file:
    s = 'XYZ'
    while s in st:
        s += 'XYZ'
    while s not in st:
        s = s[:-1]
    k = max(k, len(s))
print(k)
