data = "Andy,Larry,Tom,Jack,Li,Scott"
names = data.split(",")

ln = names[0]
for n in names[1:]:
    if len(n) > len(ln):
        ln = n

print(ln)

