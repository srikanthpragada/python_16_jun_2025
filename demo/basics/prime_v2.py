
num = int(input("Enter  a number :"))
for i in range(2, num//2 + 1):
    if num % i == 0:   # found a factor
        print('Not prime')
        break
else:
    print('Prime number')