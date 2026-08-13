# 8. Nested tuple containing student details
students = (
    (1, "Sanchita", "CSE"),
    (2, "Aarav", "CSE"),
    (3, "Priya", "IT")
)

for student in students:
    print("Roll No:", student[0], "Name:", student[1], "Department:", student[2])
