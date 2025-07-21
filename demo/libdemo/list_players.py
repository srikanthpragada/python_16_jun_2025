from datetime import *
f = open("players.txt", "rt")

players = []
for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    # remove leading and trailing whitespaces
    dobstr = parts[1].strip()
    try:
        dob = datetime.strptime(dobstr, '%d-%m-%Y')
        td = datetime.today() - dob
        age = td.days // 365
        print(name, age)
        players.append((age, name))
    except:
        pass

f.close()

for age, name in sorted(players):
    print(f"{name:20}  {age:2}")
