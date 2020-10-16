def proverka(x):
    if str(x).count("7") < 2:
        return False
    if x % 17 != 0:
        return False
    return True


a = []
for i in range(333666, 666999+1):
    if proverka(i):
        a.append(i)
print(max(a), len(a))