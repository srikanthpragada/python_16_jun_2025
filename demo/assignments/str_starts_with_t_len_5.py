def filter_string(s):
    return  s.startswith('T') and len(s) >= 5

names = ['Jackson', 'Thompson', 'Jason', 'Terry', 'Tom', 'Anderson']

for s in filter(filter_string, names):
    print(s)



