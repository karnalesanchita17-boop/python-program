 #1. Student Class

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)


s1 = Student(1, "Rahul", [80, 75, 90])
s2 = Student(2, "Amit", [70, 85, 80])

s1.display()
s2.display()


# 2. Employee Class

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross = self.basic_salary + hra + da
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)


e = Employee(101, "Rahul", 30000)
e.calculate()


# 3. Rectangle Class

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())


# 4. Circle Class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(7)
print("Area:", c.area())
print("Circumference:", c.circumference())


# 5. Book Class

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


b1 = Book(1, "Python", "John", 500)
b2 = Book(2, "Java", "James", 600)
b3 = Book(3, "C++", "Bjarne", 700)

b1.display()
b2.display()
b3.display()


# 6. Electricity Bill

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = 100 * 2 + (self.units - 100) * 3
        else:
            bill = 100 * 2 + 100 * 3 + (self.units - 200) * 5
        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Electricity Bill:", self.calculate_bill())


e = ElectricityBill(101, "Rahul", 250)
e.display()


# 7. Mobile Phone

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self, discount):
        return self.price - (self.price * discount / 100)


m = MobilePhone("Samsung", "S24", "128 GB", 50000)
m.display()
print("Price after discount:", m.discount_price(10))


# 8. Patient

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_fee):
        return self.consultation_fee + medicine_fee


p = Patient(1, "Rahul", 20, "Fever", 500)
p.display()
print("Total Bill:", p.total_bill(1000))


# 9. ATM Class

class ATM:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def display_account(self):
        print("Name:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


a = ATM("Rahul", 12345, 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount: "))
        a.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount: "))
        a.withdraw(amount)
    elif choice == 4:
        a.display_account()
    elif choice == 5:
        break
    else:
        print("Invalid choice")


# 10. Vehicle

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully")

    def rental_charges(self, days):
        return self.rental_rate * days


v = Vehicle("MH12AB1234", "Swift", 1500, True)
v.rent()
print("Rental Charges:", v.rental_charges(3))
v.return_vehicle()


# 11. Shopping Cart

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print("Product removed")
                return
        print("Product not found")

    def total_bill(self):
        total = 0
        for product in self.products:
            total = total + product[1]
        return total

    def __del__(self):
        print("Shopping cart object destroyed")


cart = ShoppingCart("Rahul", 101)
cart.add_product("Book", 500)
cart.add_product("Pen", 50)
cart.add_product("Bag", 1000)

print("Customer Name:", cart.customer_name)
print("Cart ID:", cart.cart_id)
print("Total Bill:", cart.total_bill())

cart.remove_product("Pen")
print("Total Bill:", cart.total_bill())


# 12. Food Order

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Order completed")


order = FoodOrder(101, "Rahul", "Pizza", 2, 300)
order.display()


# 13. Student Result

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "Fail"

    def __del__(self):
        print("Student result object destroyed")


s = StudentResult("Rahul", [80, 75, 70, 85, 90])

print("Name:", s.name)
print("Total:", s.total())
print("Percentage:", s.percentage())
print("Grade:", s.grade())
