def ispositive(n):
    return n > 0


lst = [10, -20, 15, -3, -4, 50]

for n in filter(ispositive, lst):
    print(n)




