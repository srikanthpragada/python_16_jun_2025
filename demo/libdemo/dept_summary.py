
f = open("salaries.txt", "rt")

dept = {}

for line in f.readlines():
    parts = line.strip().split(",")
    # if line doesn't contain 3 parts then ignore that line
    if len(parts) < 3:
        continue
    deptname, empname, salary = parts

    values = dept.get(deptname, ([],[]))
    values[0].append(empname)
    values[1].append(int(salary))
    dept[deptname] = values


f.close()
print(dept)


for key, value in dept.items():
    employees = ",".join(value[0])
    totalsalary = sum(value[1])
    print(f"{key:5}  {employees}  {totalsalary}")
