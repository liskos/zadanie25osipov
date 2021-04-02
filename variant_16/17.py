a = []
for i in range(1200,11201):
    if i %5 == 0 or i%7!=0 or i%13!=0 or i%17!=0 or i%19!=0:
        a.append(i)
print(len(a), min(a))
