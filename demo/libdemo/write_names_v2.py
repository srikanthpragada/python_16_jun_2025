names = ['Steve', 'Marshall', 'Micheal', 'Jason']

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")




