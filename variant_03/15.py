def proverka(a):
    for x in range(0, 150):
        for y in range(0, 150):
            if not ((y + 3 * x < a) or (x > 20) or (y > 40)):
                return False
    return True


for a in range(-150, 150):
    if proverka(a):
        print(a)
        break
