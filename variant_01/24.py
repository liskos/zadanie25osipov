file = open(file="Задание 24/24.txt", mode="r", encoding="utf8")
last_symbol = ""
max_length = 0
length = 0
for line in file:
    for sym in line:
        if sym == last_symbol:
            length += 1
        else:
            length = 1
        max_length = max(max_length, length)
        last_symbol = sym
print(max_length)
