a = []
for x in 'BEGK':
    for y in 'BEGK':
        for z in 'BEGK':
            for w in 'BEGK':
                s = x + y + z + w
                if s.count('E') == 2:
                    a.append(s)
print(len(a))
