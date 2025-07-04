g = 100  # Global
def f1():
    e = 1  #Enclosing
    print('F1')

    def f2():
        nonlocal  e
        e = 10
        l = 2  # local
        print('F2')
        print(g, e, l)

    f2()
    print(e)


f1()
