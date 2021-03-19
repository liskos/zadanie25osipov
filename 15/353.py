def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x)>=9) or ((5*y)>=x) or ((2*x*y)<a)):
                return False
    return True


for i in range(-10000, 10000, -1):
    if f(i):
        print(i)
        break
#программа не работает, решал сам по: ((x)>=9) or ((5*y)>=x) or ((2*x*y)<a)