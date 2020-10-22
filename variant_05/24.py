file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
for i in file:
    k = i.count('OCK') - i.count('STOCK')
print(k)
