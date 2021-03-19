k = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        if not((x>5)and((x+y)>=4)or(y>=5)):
            k+=1
print(k)
