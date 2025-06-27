st = "how do you do today"

freq = {}
for c in set(st):
     freq[c] = st.count(c)

#print(freq)

for k, v in freq.items():
    if v > 1:
        print(k)



