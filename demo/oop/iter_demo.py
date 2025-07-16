
l  = [1,2,3]

for n in l:
    print(n)

li = iter(l)
while True:
    try:
        v = next(li)
        print(v)
    except:
        break

