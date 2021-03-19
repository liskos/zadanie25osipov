k = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        if not((x>6)and((x+y)>=5)or(y>=5)):
            k+=1
print(k)
