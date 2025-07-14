
data = input("Enter number :")
try:
    num = int(data)
    print(100 // num)
except ValueError as ex:
    print('Sorry! Invalid Number!')
except ZeroDivisionError as ex:
    print('Zero is not valid number!')
except Exception as ex:
    print(ex)
else:
    print("Else block")


print("End")

