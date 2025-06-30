def wish(message, user):
    print(message, user)


# Positional params
wish('Good Morning', "Larry")
wish('Good Bye', "Tom")

# keyword args
wish(user = "Mark", message = "Hello")
wish("Hello")
