def proverka(a):
    for x in range(0, 300):
        for y in range(0, 300):
            f = (not (x > 8) or (x*x + 3*x >= a)) and (not (y*y + 5*y > a) or (y >= 4))
            if not f:
                return False
    return True

mas = []
for a in range(0, 1000):
    if proverka(a):
        mas.append(a)
        print(a)
print()
print(len(mas))