file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
l = 0
a = []
for i in file:
    if k + int(i) >= 10:
        l += 1
    else:
        a.append(l)
        l = 0
    k = int(i)
print(max(a))
