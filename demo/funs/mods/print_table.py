import sys

if len(sys.argv) < 2:
    print('Missing number!')
    print("Usage : python print_table.py <number>")
    exit(1)

num = int(sys.argv[1])


for n in range(1, 11):
    print(f"{num:3}  * {n:2}  = {num * n:5}")

