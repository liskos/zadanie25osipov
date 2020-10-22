a = []
for a1 in 'абинет':
    for a2 in 'кабинет':
        for a3 in 'кабинет':
            for a4 in 'кабинет':
                for a5 in 'кабинет':
                    for a6 in 'кабинет':
                        for a7 in 'кабинет':
                            a.append(a1 + a2 + a3 + a4 + a5 + a6 + a7)
k = 0
for i in a:
    if 'еа' in i:
        k = k
    else:
        k += 1
print(k)
