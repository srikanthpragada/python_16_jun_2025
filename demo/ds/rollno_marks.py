
data = [ (1,90), (1,80), (3, 45), (2, 40), (3, 87)]

students = {}
for rollno, marks in data:
    marks_list = students.get(rollno, [])
    marks_list.append(marks)
    students[rollno] = marks_list

print(students)
