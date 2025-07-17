import os

entries = os.walk(r"c:\classroom\python\demo")

count = 0
for dirname, folders, files in entries:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
            count +=1

print('Count =', count)

