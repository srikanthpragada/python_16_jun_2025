import json

person = {'name' : "Kevin",
          'salary' : 100000,
          'desg' : "Programmer"}

f = open("person.json", "wt")
print(json.dumps(person))
json.dump(person, f)
f.close()

