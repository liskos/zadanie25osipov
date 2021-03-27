file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
for s in file:
    b = s.count('B')
    a = s.count('A')
    S = len(s)
    if b/a >=1.05:
        k+=1
print(k)
