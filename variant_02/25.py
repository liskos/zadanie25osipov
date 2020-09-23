def proverka(n):
    global kubs
    count = 0
    max_del = 0
    for delit in kubs:
        if n % delit == 0:
            count += 1
            max_del = delit
    return count, max_del


kubs = []
for i in range(3, 81, 2):
    kubs.append(i**3)
a = []
for i in range(228224, 531136):
    count, max_del = proverka(i)
    if count >= 4:
        a.append((i, count, max_del))
for x, count, max_del in a:
    print(count, max_del)

