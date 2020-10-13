def proverka(x):
    a = []
    for delit in range(10, 100):
        if x % delit == 0:
            a.append(delit)
    if a:
        return len(a), min(a), max(a)
    return 0, 0, 0


for i in range(333555, 777999+1):
    count_del, little, big = proverka(i)
    if count_del == 35:
        print(little, big)