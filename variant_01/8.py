count = 0
for s1 in ["З", "И", "К", "Л", "М", "Н"]:
    for s2 in ["З", "И", "К", "Л", "М", "Н"]:
        for s3 in ["З", "И", "К", "Л", "М", "Н"]:
            s = s1 + s2 + s3
            if s.count("З") == 1:
                count += 1
print(count)