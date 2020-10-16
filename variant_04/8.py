i = 0
for s1 in "АЛГОРИТМ":
    for s2 in "АЛГОРИТМ":
        for s3 in "АЛГОРИТМ":
            for s4 in "АЛГОРИТМ":
                s = s1 + s2 + s3 + s4
                i += 1
                print(i, s)
print("-----------")
i = 0
for s1 in "АГИЛМОРТ":
    for s2 in "АГИЛМОРТ":
        for s3 in "АГИЛМОРТ":
            for s4 in "АГИЛМОРТ":
                s = s1 + s2 + s3 + s4
                i += 1
                if s[2:] == "ИМ":
                    print(i, s)
