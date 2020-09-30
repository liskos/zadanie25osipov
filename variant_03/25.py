def proverka(x):
    mas = [int(i) for i in str(x)]
    if x % sum(mas) == 0:
        return True
    return False


a = []
for x in range(1024, 28922):
    if proverka(x):
        a.append(x)
print(sum(a))
