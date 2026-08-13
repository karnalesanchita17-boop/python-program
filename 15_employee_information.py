# 15. Store employee ID, name and salary
employees = (
    (101, "Rahul", 35000),
    (102, "Priya", 42000),
    (103, "Amit", 38000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print("-" * 25)
