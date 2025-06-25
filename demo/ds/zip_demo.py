names = ['Java', 'Python', 'C#', 'JavaScript']
versions = [24, 3.15, 9]

# for idx, n in enumerate(names):
#     print(n, versions[idx])

for n, v in zip(names, versions):
    print(n, v)
