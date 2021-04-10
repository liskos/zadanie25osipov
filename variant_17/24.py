file = open(file='Задание 24/24.txt', mode='r')
txt = file
s = 'XYZ'
while s in txt:
    s += 'XYZ'
while s not in txt:
    s = s[:-1]
print(s)