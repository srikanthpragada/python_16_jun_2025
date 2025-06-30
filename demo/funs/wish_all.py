
def wish(*users, message = 'Hi'):
     for u in users:
         print(message, u)


wish('Mark', 'Tom', 'Bill', message =  "Hello")
wish('Mark', 'Tom')

