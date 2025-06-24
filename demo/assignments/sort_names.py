
names  = []

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

names.sort(reverse=True)

print(names)

