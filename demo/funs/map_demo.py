names = ['Scott', 'Geroge', 'Ben', 'Jo']

for l in map(len, names):
    print(l)


def firstlast(st):
    return st[0] + st[-1]


for l in map(firstlast, names):
    print(l)
