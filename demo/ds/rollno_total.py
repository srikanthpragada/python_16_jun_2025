
data = [ (1,90), (1,80), (3, 45), (2, 40), (3, 87)]

students = {}
for rollno, marks in data:
    total = students.get(rollno, 0)
    total += marks
    students[rollno] = total

print(students)
