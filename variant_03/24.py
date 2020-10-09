file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
x = 0
for line in file:
    x += line.count('XYZ') + line.count('ZYX')
print(x)
