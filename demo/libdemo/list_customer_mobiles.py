
import re

with open("customers.txt", "rt") as f:
     for line in f.readlines():
         m = re.search(r'\d+', line)
         if m is None:
             continue

         if len(m.group()) == 10:
            print(m.group())


