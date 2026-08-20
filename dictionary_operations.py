# 1. Create a set containing five integers and display all elements
print("\n1. Set of five integers")
numbers = {10,20,30,40,50}
print("Set:",numbers)

# 2. Convert list with duplicate values into a set
print("\n2. Remove duplicates from a list")
lst=[10,20,10,30,20,40]
result=set(lst)
print("Original list:",lst)
print("Set:",result)

# 3. Add two new fruits to a set
print("\n3. Add fruits")
fruits = {"Apple","Mango","Banana","Orange","Grapes"}
fruits.add("Papaya")
fruits.add("Watermelon")
print("Updated fruits:",fruits)

# 4. Remove a specified number from a set
print("\n4. Remove a number")
numbers = {10,20,30,40,50}
remove_number=30
numbers.remove(remove_number)
print("After removing",remove_number,":",numbers)

# 5. Check whether a student exists in a set
print("\n5. Check student")
students = {"Rahul","Amit","Priya","Sneha","Neha"}
name = input("Enter student name: ")
if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")

# 6. Find total number of cities
print("\n6. Number of cities")
cities = {"Pune","Mumbai","Kolhapur","Delhi","Nashik"}
print("Total cities:",len(cities))

# 7. Display programming languages using for loop
print("\n7. Programming languages")
languages = {"Python","Java","C++","JavaScript","C"}
for language in languages:
    print(language)

# 8. Remove duplicate numbers using a set
print("\n8. Remove duplicate numbers")
numbers = [1,2,3,2,4,1,5,3]
unique_numbers=set(numbers)
print("Original list:",numbers)
print("Without duplicates:",unique_numbers)

# 9. Union of two sets
print("\n9. Union")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("Union:",set1|set2)

# 10. Common elements of two sets
print("\n10. Intersection")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("Common elements:",set1&set2)

# 11. Difference between two sets
print("\n11. Difference")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("First set but not second:",set1-set2)
print("Second set but not first:",set2-set1)

# 12. Elements present in either set but not both
print("\n12. Symmetric Difference")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("Symmetric difference:",set1^set2)

# 13. Check subset
print("\n13. Subset")
set1 = {1,2}
set2 = {1,2,3,4}
print("Is first set a subset of second?",set1.issubset(set2))

# 14. Check superset
print("\n14. Superset")
set1 = {1,2,3,4}
set2 = {1,2}
print("Is first set a superset of second?",set1.issuperset(set2))

# 15. Check whether sets are disjoint
print("\n15. Disjoint sets")
set1 = {1,2,3}
set2 = {4,5,6}
print("Are sets disjoint?",set1.isdisjoint(set2))

# 16. Check whether two sets are equal
print("\n16. Equal sets")
set1 = {1, 2, 3}
set2 = {3, 2, 1}
print("Are sets equal?",set1==set2)

# 17. Subjects studied by both students
print("\n17. Common subjects")
student1 = {"Python","Java","Maths","DBMS"}
student2 = {"Java","DBMS","OS","CN"}
print("Subjects studied by both:",student1 & student2)

# 18. Display unique words from a sentence
print("\n18. Unique words")
sentence = input("Enter a sentence: ")
words = set(sentence.split())
print("Unique words:",words)

# 19. Morning and afternoon attendance
print("\n19. Session attendance")
morning = {"Amit","Rahul","Priya","Sneha","Neha"}
afternoon = {"Priya","Sneha","Rohit","Kiran","Neha"}
print("Present in both sessions:",morning & afternoon)
print("Only morning:",morning-afternoon)
print("Only afternoon:",afternoon-morning)
print("At least one session:",morning|afternoon)

# 20 & 21. Students enrolled in Python and Java
print("\n20-21. Course enrollment")
python_students = {"Amit","Rahul","Priya","Sneha"}
java_students = {"Priya","Sneha","Rohit","Kiran"}
print("Python students:",python_students)
print("Java students:",java_students)
print("Students in both courses:",python_students & java_students)
only_one_course = python_students ^ java_students
print("Students in only one course:", only_one_course)

# 22. Technical skills of two employees
print("\n22. Employee technical skils")
employee1 = {"Python","Java","SQL", "Git"}
employee2 = {"Python","C++","SQL","Docker"}
print("Common skills:", employee1 & employee2)
print("Skills unique to Employee 1:",employee1-employee2)
print("Skills unique to Employee 2:",employee2-employee1)
print("All available skills:",employee1|employee2)

# 23. Available and requested books
print("\n23. Book availability")
available_books={
    "Python Basics",
    "Java Programming",
    "Data Structures",
    "DBMS",
    "Operating Systems"
}
requested_books={
    "Python Basics",
    "DBMS",
    "Computer Networks"
}
available_requested=available_books & requested_books
print("Requested books that are available:",available_requested)

# 24. Visitor IDs from two different days
print("\n24. Visitor IDs")
day1 = {101,102,103,104,105}
day2 = {103,104,105,106,107}
print("Unique visitors:",day1|day2)
print("Returning visitors:",day1&day2)
print("Only first day:", day1-day2)
print("Only second day:", day2-day1)

# Products belonging to two categories
print("\nProducts belonging to both categories")
electronics = {"Laptop","Mobile","Tablet","Headphones"}
accessories = {"Mobile","Headphones","Charger","USB Cable"}
print("Products in both categories:",electronics & accessories)

# 25. Friends of two users
print("\n25. Friends")
user1 = {"Amit","Rahul","Priya","Sneha","Neha"}
user2 = {"Priya","Sneha","Rohit","Kiran","Neha"}
print("Mutual friends:",user1 & user2)
print("Friends unique to User 1:",user1-user2)
print("Friends unique to User 2:",user2-user1)
print("Total unique friends:",len(user1 | user2))
print("All unique friends:",user1 | user2)

#operations 
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # Union
print(A & B)   # Common elements
print(A - B)   # Only A
print(A ^ B)   # Either A or B, but not both