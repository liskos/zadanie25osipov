file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
for s in file:
    k += s.count("XXXXXXXXXX")
    k += s.count("YYYYYYY")
    k += s.count("ZZZZZ")
print(k)
