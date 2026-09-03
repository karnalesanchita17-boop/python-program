# PROGRAMS ON LAMBDA FUNCTION

# 1. Lambda function to calculate square
def q1():
    n = float(input("Enter a number: "))
    square = lambda x: x * x
    print("Square:", square(n))

# 2. Lambda function to calculate cube
def q2():
    n = float(input("Enter a number: "))
    cube = lambda x: x ** 3
    print("Cube:", cube(n))

# 3. Lambda function to check even
def q3():
    n = int(input("Enter a number: "))
    even = lambda x: x % 2 == 0
    print("Even:", even(n))

# 4. Lambda function to find maximum of two numbers
def q4():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    maximum = lambda x, y: x if x > y else y
    print("Maximum:", maximum(a, b))

# 5. Lambda function for Simple Interest
def q5():
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time: "))
    simple_interest = lambda p, r, t: (p * r * t) / 100
    print("Simple Interest:", simple_interest(p, r, t))

# 6. map() + lambda to find squares
def q6():
    numbers = list(map(int, input("Enter numbers: ").split()))
    squares = list(map(lambda x: x ** 2, numbers))
    print("Squares:", squares)

# 7. map() + lambda to find cubes
def q7():
    numbers = list(map(int, input("Enter numbers: ").split()))
    cubes = list(map(lambda x: x ** 3, numbers))
    print("Cubes:", cubes)

# 8. map() + lambda to add corresponding elements
def q8():
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))
    result = list(map(lambda x, y: x + y, list1, list2))
    print("Sum of corresponding elements:", result)

# 9. filter() + lambda to find even numbers
def q9():
    numbers = list(map(int, input("Enter numbers: ").split()))
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", even)

# 10. filter() + lambda to find prime numbers
def q10():
    numbers = list(map(int, input("Enter numbers: ").split()))
    prime = list(filter(
        lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)),
        numbers
    ))
    print("Prime numbers:", prime)

# 11. filter() + lambda to find positive numbers
def q11():
    numbers = list(map(int, input("Enter numbers: ").split()))
    positive = list(filter(lambda x: x > 0, numbers))
    print("Positive numbers:", positive)

# 12. filter() + lambda to find numbers greater than 50
def q12():
    numbers = list(map(int, input("Enter numbers: ").split()))
    result = list(filter(lambda x: x > 50, numbers))
    print("Numbers greater than 50:", result)

# 13. filter() + lambda for words > 5 characters
def q13():
    words = input("Enter words separated by space: ").split()
    result = list(filter(lambda word: len(word) > 5, words))
    print("Words having more than 5 characters:")
    print(result)

# 14. Sort words according to length using lambda
def q14():
    words = input("Enter words separated by space: ").split()
    result = sorted(words, key=lambda word: len(word))
    print("Words sorted by length:")
    print(result)

# 15. Sort students according to marks
def q15():
    students = [
        ("Amit", 85),
        ("Priya", 92),
        ("Rahul", 78),
        ("Sneha", 88)
    ]
    result = sorted(students, key=lambda student: student[1])
    print("Students sorted according to marks:")
    for student in result:
        print(student)

# 16. Sort employees according to salary
def q16():
    employees = [
        ("Amit", 45000),
        ("Priya", 65000),
        ("Rahul", 50000),
        ("Sneha", 75000)
    ]
    result = sorted(employees, key=lambda employee: employee[1])
    print("Employees sorted according to salary:")
    for employee in result:
        print(employee)

# 17. Student processing using functions and lambda
def q17():
    students = [
        ("Amit", 85),
        ("Priya", 92),
        ("Rahul", 68),
        ("Sneha", 78),
        ("Neha", 72)
    ]
    # a) Average marks
    average = sum(map(lambda s: s[1], students)) / len(students)
    # b) Students scoring above 75
    above_75 = list(
        filter(lambda s: s[1] > 75, students)
    )
    # c) Sort according to marks
    sorted_students = sorted(
        students,
        key=lambda s: s[1]
    )
    print("Average Marks:", average)
    print("\nStudents scoring above 75:")
    for student in above_75:
        print(student)
    print("\nStudents sorted according to marks:")
    for student in sorted_students:
        print(student)

# 18. Employee processing using filter(), map(), sorted()
def q18():
    employees = [
        ("Amit", "IT", 45000),
        ("Priya", "HR", 65000),
        ("Rahul", "IT", 55000),
        ("Sneha", "Finance", 70000)
    ]
    # a) Employees earning more than 50000
    high_salary = list(
        filter(lambda e: e[2] > 50000, employees)
    )zz
    # b) Increase salary by 10%
    increased_salary = list(
        map(
            lambda e: (e[0], e[1], e[2] * 1.10),
            employees
        )
    )
    # c) Sort employees according to salary
    sorted_employees = sorted(
        employees,
        key=lambda e: e[2]
    )
    print("Employees earning more than ₹50,000:")
    for employee in high_salary:
        print(employee)
    print("\nSalaries after 10% increase:")
    for employee in increased_salary:
        print(employee)
    print("\nEmployees sorted according to salary:")
    for employee in sorted_employees:
        print(employee)

# 19. Product processing using lambda
def q19():
    products = [
        ("Laptop", 50000, 2),
        ("Mouse", 800, 3),
        ("Keyboard", 1500, 2),
        ("Monitor", 12000, 1)
    ]
    # a) Calculate total value
    total_values = list(
        map(
            lambda p: (p[0], p[1], p[2], p[1] * p[2]),
            products
        )
    )
    # b) Products costing more than ₹1000
    expensive = list(
        filter(lambda p: p[1] > 1000, products)
    )
    # c) Sort according to total value
    sorted_products = sorted(
        total_values,
        key=lambda p: p[3]
    )
    print("Total value of each product:")
    for product in total_values:
        print(product)
    print("\nProducts costing more than ₹1000:")
    for product in expensive:
        print(product)
    print("\nProducts sorted according to total value:")
    for product in sorted_products:
        print(product)

# 20. Word processing using map(), filter(), sorted()
def q20():
    words = input("Enter words separated by space: ").split()
    # a) Length of every word
    lengths = list(
        map(lambda word: len(word), words)
    )
    # b) Words having more than 5 characters
    long_words = list(
        filter(lambda word: len(word) > 5, words)
    )
    # c) Sort according to length
    sorted_words = sorted(
        words,
        key=lambda word: len(word)
    )
    print("\nLength of every word:")
    print(lengths)
    print("\nWords having more than 5 characters:")
    print(long_words)
    print("\nWords sorted according to length:")
    print(sorted_words)

# MAIN MENU
while True:
    print("LAMBDA FUNCTION PROGRAMS")
    print("1.  Square of a number")
    print("2.  Cube of a number")
    print("3.  Check even number")
    print("4.  Maximum of two numbers")
    print("5.  Simple Interest")
    print("6.  Square using map()")
    print("7.  Cube using map()")
    print("8.  Sum of corresponding list elements")
    print("9.  Even numbers using filter()")
    print("10. Prime numbers using filter()")
    print("11. Positive numbers using filter()")
    print("12. Numbers greater than 50")
    print("13. Words having more than 5 characters")
    print("14. Sort words according to length")
    print("15. Sort students according to marks")
    print("16. Sort employees according to salary")
    print("17. Student processing")
    print("18. Employee processing")
    print("19. Product processing")
    print("20. Word processing")
    print("0.  Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        q1()

    elif choice == "2":
        q2()

    elif choice == "3":
        q3()

    elif choice == "4":
        q4()

    elif choice == "5":
        q5()

    elif choice == "6":
        q6()

    elif choice == "7":
        q7()

    elif choice == "8":
        q8()

    elif choice == "9":
        q9()

    elif choice == "10":
        q10()

    elif choice == "11":
        q11()

    elif choice == "12":
        q12()

    elif choice == "13":
        q13()

    elif choice == "14":
        q14()

    elif choice == "15":
        q15()

    elif choice == "16":
        q16()

    elif choice == "17":
        q17()

    elif choice == "18":
        q18()

    elif choice == "19":
        q19()

    elif choice == "20":
        q20()

    elif choice == "0":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")

