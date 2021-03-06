def es(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def delit(x):
    k = 0
    for i in range(2, int(x**0.5) +1):
        if es(i) and x//i == 0:
            if x//i == x//(x//i):
                k += 1
            else:
                k +=2
    if k < 6:
        return False
    return True


for i in range(25317,51238):
    if delit(i):
        print(i)
#???