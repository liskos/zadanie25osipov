def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((2*x+3*y)!=13)or((2*y+3*x)!=12)or((x*x+3*x-1)<a)and((2*y*y-4*y+20)>a)):
                return False
    return True


k = 0
for i in range(10000, -10000, -1):
    if f(i):
        k+= 1
print(k)
