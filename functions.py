# Python Program Using Functions

# 1. Factorial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

n = int(input("1. Enter number for factorial: "))
print("Factorial =", factorial(n))


# 2. Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("\n2. Enter number: "))
print("Number is", check_even_odd(n))


# 3. Greater of two numbers
def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("\n3. Enter first number: "))
b = int(input("Enter second number: "))
print("Greater number =", greater(a, b))


# 4. Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("\n4. Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))


# 5. Prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("\n5. Enter number: "))
print("Prime =", is_prime(n))


# 6. Area of circle
def circle_area(r):
    return 3.14 * r * r

r = float(input("\n6. Enter radius: "))
print("Area of circle =", circle_area(r))


# 7. Sum of first n natural numbers
def natural_sum(n):
    s = 0

    for i in range(1, n + 1):
        s = s + i

    return s

n = int(input("\n7. Enter n: "))
print("Sum =", natural_sum(n))


# 8. Power
def power(base, exponent):
    return base ** exponent

base = int(input("\n8. Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power =", power(base, exponent))


# 9. Largest element without max()
def largest(numbers):
    big = numbers[0]

    for i in numbers:
        if i > big:
            big = i

    return big

numbers = list(map(int, input("\n9. Enter numbers: ").split()))
print("Largest =", largest(numbers))


# 10. Count vowels
def count_vowels(s):
    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

s = input("\n10. Enter string: ")
print("Number of vowels =", count_vowels(s))


# 11. Reverse string
def reverse_string(s):
    return s[::-1]

s = input("\n11. Enter string: ")
print("Reverse =", reverse_string(s))


# 12. Palindrome
def palindrome(x):
    x = str(x)

    if x == x[::-1]:
        return True
    else:
        return False

x = input("\n12. Enter string or number: ")
print("Palindrome =", palindrome(x))


# 13. Average of list
def list_average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(float, input("\n13. Enter numbers: ").split()))
print("Average =", list_average(numbers))


# 14. Count occurrence
def occurrence(numbers, x):
    count = 0

    for i in numbers:
        if i == x:
            count = count + 1

    return count

numbers = list(map(int, input("\n14. Enter numbers: ").split()))
x = int(input("Enter element: "))
print("Occurrence =", occurrence(numbers, x))


# 15. Unique elements
def unique(numbers):
    result = []

    for i in numbers:
        if i not in result:
            result.append(i)

    return result

numbers = list(map(int, input("\n15. Enter numbers: ").split()))
print("Unique elements =", unique(numbers))


# 16. Second largest
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

numbers = list(map(int, input("\n16. Enter numbers: ").split()))
print("Second largest =", second_largest(numbers))


# 17. Fibonacci
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("\n17. Enter n: "))
print("Fibonacci =", fibonacci(n))


# 18. Percentage and Grade
def percentage_grade(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("\n18. Enter marks: ")))

percentage, grade = percentage_grade(marks)

print("Percentage =", percentage)
print("Grade =", grade)


# 19. Electricity bill
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12

    return bill

units = float(input("\n19. Enter units consumed: "))
print("Electricity Bill =", electricity_bill(units))


# 20. Gross salary
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da

basic = float(input("\n20. Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))


# 21. Shopping bill
def shopping_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    if total >= 5000:
        discount = total * 0.20
    elif total >= 3000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

n = int(input("\n21. Enter number of items: "))

prices = []
quantities = []

for i in range(n):
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    prices.append(price)
    quantities.append(quantity)

print("Final Bill =", shopping_bill(prices, quantities))


# 22. Minimum, Maximum, Sum and Average
def statistics(numbers):
    small = numbers[0]
    big = numbers[0]
    total = 0

    for i in numbers:
        if i < small:
            small = i

        if i > big:
            big = i

        total = total + i

    avg = total / len(numbers)

    return small, big, total, avg

numbers = list(map(int, input("\n22. Enter numbers: ").split()))

small, big, total, avg = statistics(numbers)

print("Minimum =", small)
print("Maximum =", big)
print("Sum =", total)
print("Average =", avg)


# 23. Student Records
def student_record(name, roll, marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    return total, percentage, grade

n = int(input("\n23. Enter number of students: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    marks = []

    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total, percentage, grade = student_record(name, roll, marks)

    students.append([name, roll, total, percentage, grade])

print("\nStudent Records:")

for student in students:
    print(student)

total_percentage = 0
highest = students[0]
lowest = students[0]

for student in students:
    total_percentage = total_percentage + student[3]

    if student[3] > highest[3]:
        highest = student

    if student[3] < lowest[3]:
        lowest = student

print("Class Average =", total_percentage / n)
print("Highest Scorer =", highest[0])
print("Lowest Scorer =", lowest[0])


# 24. Bank System
balance = 0
history = []

def deposit(amount):
    global balance
    balance = balance + amount
    history.append("Deposit " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        history.append("Withdrawal " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

def balance_enquiry():
    print("Balance =", balance)

def transaction_history():
    print("Transaction History:")
    for i in history:
        print(i)

print("\n24. Bank System")

amount = float(input("Enter deposit amount: "))
deposit(amount)

amount = float(input("Enter withdrawal amount: "))
withdrawal(amount)

balance_enquiry()
transaction_history()


# 25. Library Management
books = {}

def add_book(book_id, name):
    books[book_id] = {"name": name, "available": True}

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")

def search_book(name):
    for book_id in books:
        if books[book_id]["name"].lower() == name.lower():
            print("Book found")

def available_books():
    print("Available books:")
    for book_id in books:
        if books[book_id]["available"]:
            print(book_id, books[book_id]["name"])

print("\n25. Library")

book_id = input("Enter book id: ")
name = input("Enter book name: ")

add_book(book_id, name)
available_books()

issue_book(book_id)
available_books()

return_book(book_id)
available_books()


# 26. Modular Electricity Bill
def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 500 + (units - 100) * 7
    else:
        bill = 1200 + (units - 200) * 10

    return bill

def fixed_charge():
    return 100

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    if amount > 2000:
        return amount * 0.05
    return 0

units = float(input("\n26. Enter units: "))

bill = calculate_bill(units)
fixed = fixed_charge()
tax = calculate_tax(bill + fixed)
discount = calculate_discount(bill + fixed)

final_bill = bill + fixed + tax - discount

print("Energy Bill =", bill)
print("Fixed Charge =", fixed)
print("Tax =", tax)
print("Discount =", discount)
print("Final Bill =", final_bill)


# 27. Hospital Bill
def consultation_charge(amount):
    return amount

def laboratory_charge(amount):
    return amount

def medicine_charge(amount):
    return amount

def room_charge(amount):
    return amount

def hospital_bill(c, l, m, r, category):
    total = c + l + m + r

    if category == "senior":
        discount = total * 0.20
    elif category == "child":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

print("\n27. Hospital Bill")

c = float(input("Consultation charges: "))
l = float(input("Laboratory charges: "))
m = float(input("Medicine charges: "))
r = float(input("Room charges: "))
category = input("Patient category: ")

print("Final Bill =", hospital_bill(c, l, m, r, category))


# 28. Product Invoice
products = {}

def add_product(name, price, quantity):
    products[name] = price * quantity

def remove_product(name):
    if name in products:
        del products[name]

def subtotal():
    return sum(products.values())

def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    elif coupon == "SAVE20":
        return amount * 0.20
    return 0

def calculate_gst(amount):
    return amount * 0.18

def final_invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    amount = sub - discount
    gst = calculate_gst(amount)

    return amount + gst

print("\n28. Product Invoice")

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    add_product(name, price, quantity)

coupon = input("Enter coupon: ")

print("Subtotal =", subtotal())
print("Final Invoice =", final_invoice(coupon))


# 29. Recursive Binary Search
def binary_search(a, low, high, x):
    if low > high:
        return -1

    mid = (low + high) // 2

    if a[mid] == x:
        return mid

    elif x < a[mid]:
        return binary_search(a, low, mid - 1, x)

    else:
        return binary_search(a, mid + 1, high, x)

a = list(map(int, input("\n29. Enter sorted numbers: ").split()))
x = int(input("Enter element to search: "))

result = binary_search(a, 0, len(a) - 1, x)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)


# 30. Decimal to Binary using Recursion
def decimal_binary(n):
    if n == 0:
        return ""

    return decimal_binary(n // 2) + str(n % 2)

n = int(input("\n30. Enter decimal number: "))

if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_binary(n))


# 31. Recursive Palindrome
def recursive_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return recursive_palindrome(s[1:-1])

s = input("\n31. Enter string: ")

if recursive_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")


# 32. Calculator using functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

print("\n32. Calculator")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", calculate(a, b, addition))
print("Subtraction =", calculate(a, b, subtraction))
print("Multiplication =", calculate(a, b, multiplication))

if b != 0:
    print("Division =", calculate(a, b, division))
else:
    print("Division not possible")