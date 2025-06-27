
names = ['Scott', 'Steve', 'Larry', 'Richards']

chars = set()
for n in names:
    chars = chars | set(n)

print(chars)

