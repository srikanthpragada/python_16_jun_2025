
num = int(input("Enter  a number :"))
isprime = True

for i in range(2, num//2 + 1):
    if num % i == 0:   # found a factor
        print('Not prime')
        isprime = False
        break

if isprime:
    print('Prime number')