def extract_upper(s):
    st = ''
    for c in s:
        if c.isupper():
            st += c
    return st

def extract_upper2(s):
    return ''.join( filter(str.isupper,s))

names = ['JackSon', 'ThompSon', 'JasoN', 'TErry', 'Tom', 'Anderson']

for s in map(extract_upper2, names):
    print(s)
