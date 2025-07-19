import re

with  open("ghibli.txt", "rt") as f:
    contents = f.read()

new_contents = re.sub(' +', ' ', contents)

with  open("ghibli.txt", "wt") as f:
    f.write(new_contents)

