import os

entries = os.walk(r"c:\classroom\python\demo")

for dirname, folders, files in entries:
    print(dirname)
    print("*" * 50)
    for file in files:
        print(file)
