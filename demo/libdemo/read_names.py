f = open("names.txt", "rt")

for name in f.readlines():
    print(name.strip())

f.close()
