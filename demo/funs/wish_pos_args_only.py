# Positional only args
def wish(message, user, /):
    print(message, user)


# wish(user="Mark", message="Hello")
wish("Hello", "Scott")
