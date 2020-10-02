a = []
prost = [2]
for i in range(3, 289213):
    for pr in prost:
        if i % pr == 0:
            break
    else:
        prost.append(i)
answer = []
for i in prost:
    if 1024 <= i <= 289212:
        answer.append(i)
print(sum(answer))
