# Assume d may have any one of the following two structures
#d = {'name': 'Jack', 'email': 'jack@gmail.com'}
#d = {'firstname': 'Scott'}
d = {'uname': 'Scott'}

match d:
    case {'name': user}:
        pass
    case {'firstname': user}:
        pass
    case _:
        user = 'Unknown'

print(user)