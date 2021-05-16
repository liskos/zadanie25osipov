file = open(file='Задание 24/24.txt')
mk = 0
st = ''
for s in file:
    for i in s:
        if 'XZZY' not in st:
            st += i
            k = len(st)
            if k > mk:
                mk = k
        else:
            st = ''
print(mk)
