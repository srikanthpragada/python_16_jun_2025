names = ['Scott', 'Geroge', 'Ben', 'Jo']

for l in map(lambda s : s[0] + s[-1], names):
    print(l)
