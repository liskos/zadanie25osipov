def proverka(a):
    for x in range(0, 150):
        for y in range(0, 150):
            if not((not(x <= 9) or (x*x < a)) and (not(y*y < a) or (y < 12))):
                return False
    return True


for i in range(-100, 100):
    if proverka(i):
        print(i)
