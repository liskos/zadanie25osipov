def es(x):
    mas_prost = [2]
    for i in range(2, x+1):
        for prost in mas_prost:
            if i % prost == 0:
                break
        else:
            mas_prost.append(i)
    return mas_prost


prost = es(51238)
print(prost)

for i in range(25317,51238):
    a = []
    for pro in prost:
        if i % pro == 0 and i != pro:
            a.append(pro)
    if len(a) >= 6:

        print(i, max(a))
