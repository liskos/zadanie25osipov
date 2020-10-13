def twosev(x):
    x = str(x)
    if '7' in x:
        x = x.replace('7', '0', 1)
        if '7' in x:
            return True
        else:
            return False
    else:
        return False


a = []
for i in range(333666, 667000):
    if twosev(i) == True and i % 17 == 0:
        a.append(i)
print(max(a), len(a))
