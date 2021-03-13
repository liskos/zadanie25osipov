file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
l = 1
a = []
for p in file:
    for i in p:
        if k + int(i) >= 10:
            l += 1
        else:
            a.append(l)
            l = 1
        k = int(i)
print(max(a))
