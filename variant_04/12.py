a = '563' * 121
while '56' in a or '3333' in a:
    a = a.replace('56', '3', 1)
    a = a.replace('3333', '3', 1)
print(a)
