def isupper(c):
    return c.isupper()


for c in filter(isupper , "This IS good"):
    print(c)

for c in filter(str.isupper , "This IS good"):
    print(c)