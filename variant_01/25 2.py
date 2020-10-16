def simple(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


a = []
for i in range(1024, 289213):
    if simple(i):
        a.append(i)
print(sum(a))
