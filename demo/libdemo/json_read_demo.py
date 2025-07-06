import json

f = open("person.json", "rt")
d = json.load(f)
f.close()

print(d)


