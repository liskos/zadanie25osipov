file = open(file='24 (1).txt')
k, n = 0, 0
lest = ''
for s in file:
    for i in s:
        n += 1
        if i == '(' and lest == ')':
            k += 1
        if k == 10000:
            print(n - 1)
        lest = i
