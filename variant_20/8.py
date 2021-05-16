k = 0
for a1 in 'ВИНЯ':
    for a2 in 'ВИШНЯ':
        for a3 in 'ВИШНЯ':
            for a4 in 'ВИШНЯ':
                for a5 in 'ВИШНЯ':
                    for a6 in 'ВШН':
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if 'В' not in s:
                            k += 1
                        elif 'В' in s:
                            s = s.replace('В', '', 1)
                            if 'В' in s:
                                k += 1
print(k)
