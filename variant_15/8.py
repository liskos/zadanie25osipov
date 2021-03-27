#6-10
k6 = 0
for i1 in range(100000,1000000):
    s = list(map(int, str(i1)))
    if (len(set(s)) == 6 and s[0]%2 != s[1]%2 and s[1]%2 != s[2]%2 and s[2]%2 != s[3]%2 and s[3]%2 != s[4]%2
            and s[4]%2 != s[5]%2):
                            k6 += 1
print(k6)
k = 0
for i1 in range(1000,10000):
    s = str(i1)
    if s[0] != s[1] != s[2] != s[3]:
        k += 1
print(k)
print(k6-k)