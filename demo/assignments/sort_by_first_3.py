def first3(s):
    return s[:3]


names = ['Jackson', 'Thompson', 'Jason', 'Terry', 'Tom', 'Anderson']

for s in sorted(names, key=first3):
    print(s)

for s in sorted(names, key=lambda s: s[:3]):
    print(s)