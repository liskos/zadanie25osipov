file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
for i in file:
    k += i.count('X' * 6)
    k += i.count('Y' * 3)
    k += i.count('Z' * 9)
print(k)
