names = ['Steve', 'Marshall', 'Micheal', 'Jason']

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()




