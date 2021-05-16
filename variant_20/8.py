k = 0
for a1 in 'ВИНЯ':
    for a2 in 'ВИШНЯ':
        for a3 in 'ВИШНЯ':
            for a4 in 'ВИШНЯ':
                for a5 in 'ВИШНЯ':
                    for a6 in 'ВШН':
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if s.count("В") <= 1:
                                k += 1
print(k)
