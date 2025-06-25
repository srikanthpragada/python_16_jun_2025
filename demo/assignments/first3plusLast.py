
lst = []

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    if len(name) >= 4:
        lst.append(name[:3] + name[-1])


print(lst)
