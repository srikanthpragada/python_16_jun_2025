def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def math_operation(a, b, operation):
    print(operation(a, b))


math_operation(10, 20, add)
math_operation(10, 20, mul)
#math_operation(10,20, len)

