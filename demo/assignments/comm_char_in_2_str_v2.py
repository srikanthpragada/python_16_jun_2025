s1 = "abcdedad"
s2 = "defa"

found = []
for c in s1:
    if c not in found and c in s2:
        print(c)
        found.append(c)
