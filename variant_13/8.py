k = 0
for i1 in 'АВДПР':
    for i2 in 'АВДПР':
        for i3 in 'АВДПР':
            for i4 in 'АВДПР':
                i = i1 + i2 + i3 + i4
                k += 1
                if 'А' not in i and len(set(i)) == 4:
                    print(k)
                    break
