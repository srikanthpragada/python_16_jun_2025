st = "how do you do today"

found = []
for c in st:
    if c not in found:
        print(c, st.count(c))
        found.append(c)




