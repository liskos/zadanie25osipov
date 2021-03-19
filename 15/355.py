def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((-5*x+y)!=-7)or((x*x-y)!=1)or((x+3*y)>a)and((y-x)<=a)):
                return False
    return True


k = 0
for i in range(10000, -10000, -1):
    if f(i):
        k+= 1
print(k)
