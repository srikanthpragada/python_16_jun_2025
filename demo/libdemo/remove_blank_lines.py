
with open("names.txt", "rt") as f:
   selected_lines =  filter(lambda l: len(l.strip()) > 0, f.readlines())

with open("names.txt", "wt") as f:
    for line in selected_lines:
        f.write(line)

