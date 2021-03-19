k = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        if not((x>1)and((x+y)>=6)or(y>=5)):
            k+=1
print(k)
