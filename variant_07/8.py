k = 0
for a1 in 'СЛОН':
    for a2 in 'СЛОН':
        for a3 in 'СЛОН':
            a = a1 + a2 + a3
            if 'С' in a:
                a = a.replace('С', '1', 1)
                if 'С' not in a:
                    k += 1
print(k)
