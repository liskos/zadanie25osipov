def d30(n):
    digits = list(map(int, str(n)))
    digits.sort()
    max_number = digits[2] * 10 + digits[1]
    if digits[0] != 0:
        min_number = digits[0] * 10 + digits[1]
    elif digits[1] != 0:
        min_number = digits[1] * 10
    else:
        min_number = digits[2] * 10
    return max_number - min_number


mas = []
for i in range(800, 901):
    if d30(i) == 30:
        mas.append(i)
print(mas)
print(len(mas))