a = []
for x in 'BEGK':
    for y in 'BEGK':
        for z in 'BEGK':
            for w in 'BEGK':
                s = x + y + z + w
                a.append(s)
k = 0
for i in a:
    if 'E' in i:
        i = i.replace('E', '1', 1)
        if 'E' in i:
            k += 1
print(k)
