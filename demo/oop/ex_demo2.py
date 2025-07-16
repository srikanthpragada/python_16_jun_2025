a = 10
b = 0
try:
    c = a / b
    print(c)
except ValueError as ex:
    print("Error :", ex)
else:
    print("Job Done!")
finally:
    print("The End!")