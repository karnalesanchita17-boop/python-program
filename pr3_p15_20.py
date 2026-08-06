# Programs 15-20

# 15. Second largest element
numbers=[10, 50, 30, 80, 60]
largest=second=float('-inf')
for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif largest>num>second:
        second=num
print("15. Largest =", largest)
print("15. Second Largest =", second)

print("\n16. Student Details")
students = [
    ["Amit", 1, 85],
    ["Priya", 2, 90],
    ["Rahul", 3, 78]
]
for s in students:
    print("Name:", s[0], "Roll:", s[1], "Marks:", s[2])

print("\n17. Matrix Addition")
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
C = []
for i in range(3):
    row=[]
    for j in range(3):
        row.append(A[i][j]+B[i][j])
    C.append(row)
for row in C:
    print(row)

print("\n18. Shopping Cart")
cart=["Milk","Bread"]
cart.append("Eggs")
print("After Add:",cart)
if "Bread" in cart:
    cart.remove("Bread")
print("After Remove:",cart)
item="Milk"
print("Search",item,":", item in cart)
print("Display Cart:",cart)
print("Total Items:",len(cart))

print("\n19. Student Attendance")
attendance=["Amit","Priya","Rahul"]
print("Total Students:",len(attendance))
name="Priya"
print("Present?" , name in attendance)
attendance.append("Sneha")
if "Rahul" in attendance:
    attendance.remove("Rahul")
print("Updated List:",attendance)

print("\n20. Book List")
books=["Python","Java","C++"]
books.append("Data Structures")
book="Java"
print("Search:", book in books)
books.remove("C++")
print("Books:")
for b in books:
    print(b)
print("Total Books:",len(books))
