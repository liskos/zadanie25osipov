file = open(file='Задание 24/24test.txt', mode='r', encoding='utf8')
k = 0
m = 0
l = 3
for i in file:
    if int(i) % 2 != l:
        l = int(i) % 2
        if m < k:
            m = k
        k = 0
    else:
        k += 1
if m < k:
    m = k
print(m)
