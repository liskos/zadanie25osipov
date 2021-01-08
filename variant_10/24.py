file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
for i in file:
    a = i.count('XXXXX')
    a += i.count('YYYYYY')
    a += i.count('ZZZZZZZ')
print(a)
