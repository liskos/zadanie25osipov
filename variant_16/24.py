file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
l = 0
w = ''
for s in file:
    for i in s:
        if i == w:
            k += 1
        else:
            if l < k:
                l = k
            k = 0
            w = i
if l < k:
    l = k
print(l)
