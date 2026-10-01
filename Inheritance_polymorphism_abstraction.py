from abc import ABC, abstractmethod

#INHERITANCE PROGRAMS
def inheritance_1():
    print("\nQ1 Employee -> Manager ")

    class Employee:
        def __init__(self, emp_id, name, salary):
            self.emp_id = emp_id
            self.name = name
            self.salary = salary

        def display(self):
            print("Employee ID:", self.emp_id)
            print("Name:", self.name)
            print("Salary:", self.salary)

    class Manager(Employee):
        def __init__(self, emp_id, name, salary, department):
            super().__init__(emp_id, name, salary)
            self.department = department

        def display_manager(self):
            self.display()
            print("Department:", self.department)
            print("Annual Salary:", self.salary * 12)

    m = Manager(101, "Sanchita", 50000, "IT")
    m.display_manager()


def inheritance_2():
    print("\n Q2 Vehicle -> Car ")

    class Vehicle:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display(self):
            print("Brand:", self.brand)
            print("Model:", self.model)

    class Car(Vehicle):
        def __init__(self, brand, model, fuel_type, price):
            super().__init__(brand, model)
            self.fuel_type = fuel_type
            self.price = price

        def display_car(self):
            self.display()
            print("Fuel Type:", self.fuel_type)
            print("Price:", self.price)
            print("Discounted Price:", self.price * 0.9)

    c = Car("Toyota", "Innova", "Petrol", 2000000)
    c.display_car()


def inheritance_3():
    print("\n Q3 Academic + Sports -> Student")

    class Academic:
        def __init__(self, marks):
            self.marks = marks

    class Sports:
        def __init__(self, sports_points):
            self.sports_points = sports_points

    class Student(Academic, Sports):
        def __init__(self, marks, sports_points):
            Academic.__init__(self, marks)
            Sports.__init__(self, sports_points)

        def performance(self):
            print("Academic Marks:", self.marks)
            print("Sports Points:", self.sports_points)
            print("Overall Performance:", self.marks + self.sports_points)

    s = Student(85, 10)
    s.performance()


def inheritance_4():
    print("\n Q4 PersonalDetails + ProfessionalDetails -> Employee ")

    class PersonalDetails:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class ProfessionalDetails:
        def __init__(self, emp_id, designation, salary):
            self.emp_id = emp_id
            self.designation = designation
            self.salary = salary

    class Employee(PersonalDetails, ProfessionalDetails):
        def __init__(self, name, age, emp_id, designation, salary):
            PersonalDetails.__init__(self, name, age)
            ProfessionalDetails.__init__(
                self, emp_id, designation, salary
            )

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Employee ID:", self.emp_id)
            print("Designation:", self.designation)
            print("Salary:", self.salary)

    e = Employee("Sanchita", 21, 101, "Developer", 50000)
    e.display()


def inheritance_5():
    print("\n Q5 Person -> Student -> ResearchStudent ")

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, roll, course):
            super().__init__(name, age)
            self.roll = roll
            self.course = course

    class ResearchStudent(Student):
        def __init__(self, name, age, roll, course, topic, guide):
            super().__init__(name, age, roll, course)
            self.topic = topic
            self.guide = guide

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Roll No:", self.roll)
            print("Course:", self.course)
            print("Research Topic:", self.topic)
            print("Guide:", self.guide)

    r = ResearchStudent(
        "Sanchita", 21, 79, "CSE",
        "Artificial Intelligence", "Dr. Patil"
    )
    r.display()


def inheritance_6():
    print("\n Q6 BankAccount -> SavingsAccount -> PremiumSavingsAccount ")

    class BankAccount:
        def __init__(self, account_no, balance):
            self.account_no = account_no
            self.balance = balance

    class SavingsAccount(BankAccount):
        def __init__(self, account_no, balance, interest_rate):
            super().__init__(account_no, balance)
            self.interest_rate = interest_rate

    class PremiumSavingsAccount(SavingsAccount):
        def __init__(self, account_no, balance, interest_rate, benefits):
            super().__init__(account_no, balance, interest_rate)
            self.benefits = benefits

        def display(self):
            interest = self.balance * self.interest_rate / 100
            print("Account Number:", self.account_no)
            print("Balance:", self.balance)
            print("Interest Rate:", self.interest_rate, "%")
            print("Interest:", interest)
            print("Benefits:", self.benefits)

    a = PremiumSavingsAccount(
        "SB1001", 100000, 7, "Airport Lounge and Cashback"
    )
    a.display()


def inheritance_7():
    print("\nQ7 Shape -> Circle/Rectangle/Triangle")

    class Shape:
        def __init__(self, name):
            self.name = name

    class Circle(Shape):
        def __init__(self, radius):
            super().__init__("Circle")
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

    class Rectangle(Shape):
        def __init__(self, length, width):
            super().__init__("Rectangle")
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

    class Triangle(Shape):
        def __init__(self, base, height):
            super().__init__("Triangle")
            self.base = base
            self.height = height

        def area(self):
            return 0.5 * self.base * self.height

    c = Circle(5)
    r = Rectangle(10, 5)
    t = Triangle(10, 6)

    print(c.name, "Area:", c.area())
    print(r.name, "Area:", r.area())
    print(t.name, "Area:", t.area())


def inheritance_8():
    print("\n Q8 Employee -> Manager/Developer/Tester ")

    class Employee:
        def __init__(self, emp_id, name, basic_salary):
            self.emp_id = emp_id
            self.name = name
            self.basic_salary = basic_salary

    class Manager(Employee):
        def salary(self):
            return self.basic_salary + 20000

    class Developer(Employee):
        def salary(self):
            return self.basic_salary + 15000

    class Tester(Employee):
        def salary(self):
            return self.basic_salary + 10000

    employees = [
        Manager(1, "Amit", 50000),
        Developer(2, "Rahul", 45000),
        Tester(3, "Priya", 40000)
    ]

    for e in employees:
        print(e.name, "Salary:", e.salary())


def inheritance_9():
    print("\n Q9 Person -> Student/Faculty and TeachingAssistant ")

    class Person:
        def __init__(self, name):
            self.name = name

    class Student(Person):
        def study(self):
            print(self.name, "is studying.")

    class Faculty(Person):
        def teach(self):
            print(self.name, "is teaching.")

    class TeachingAssistant(Student, Faculty):
        def assist(self):
            print(self.name, "is assisting students.")

    ta = TeachingAssistant("Sanchita")
    ta.study()
    ta.teach()
    ta.assist()


def inheritance_10():
    print("\n Q10 Combination of Inheritance ")

    class Vehicle:
        def show(self):
            print("This is a vehicle.")

    class Car(Vehicle):
        def car_info(self):
            print("This is a car.")

    class Bike(Vehicle):
        def bike_info(self):
            print("This is a bike.")

    class SportsCar(Car):
        def sports(self):
            print("Sports car has high speed.")

    class ElectricBike(Bike):
        def electric(self):
            print("Electric bike runs on battery.")

    s = SportsCar()
    s.show()
    s.car_info()
    s.sports()

    print()

    e = ElectricBike()
    e.show()
    e.bike_info()
    e.electric()


def inheritance_11():
    print("\n Q11 Student -> Result ")

    class Student:
        def __init__(self, roll, name, course):
            self.roll = roll
            self.name = name
            self.course = course

    class Result(Student):
        def __init__(self, roll, name, course, marks):
            super().__init__(roll, name, course)
            self.marks = marks

        def display_result(self):
            total = sum(self.marks)
            percentage = total / 3

            if percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            else:
                grade = "D"

            print("Roll No:", self.roll)
            print("Name:", self.name)
            print("Course:", self.course)
            print("Marks:", self.marks)
            print("Total:", total)
            print("Percentage:", percentage)
            print("Grade:", grade)

    r = Result(79, "Sanchita", "CSE", [85, 78, 90])
    r.display_result()


def inheritance_12():
    print("\n- Q12 Product -> ElectronicProduct ")

    class Product:
        def __init__(self, product_id, name, price):
            self.product_id = product_id
            self.name = name
            self.price = price

    class ElectronicProduct(Product):
        def __init__(
            self, product_id, name, price, brand, warranty
        ):
            super().__init__(product_id, name, price)
            self.brand = brand
            self.warranty = warranty

        def display(self):
            print("Product ID:", self.product_id)
            print("Name:", self.name)
            print("Brand:", self.brand)
            print("Price:", self.price)
            print("Warranty:", self.warranty)
            print("Discounted Price:", self.price * 0.9)

    p = ElectronicProduct(
        101, "Laptop", 60000, "HP", "2 Years"
    )
    p.display()


def inheritance_13():
    print("\n Q13 Printer + Scanner -> MultifunctionDevice ")

    class Printer:
        def print_document(self):
            print("Printing document...")

    class Scanner:
        def scan_document(self):
            print("Scanning document...")

    class MultifunctionDevice(Printer, Scanner):
        def display(self):
            print("Multifunction Device")
            self.print_document()
            self.scan_document()

    m = MultifunctionDevice()
    m.display()


def inheritance_14():
    print("\n Q14 Camera + Phone -> Smartphone ")

    class Camera:
        def take_photo(self):
            print("Photo captured.")

    class Phone:
        def make_call(self):
            print("Calling...")

    class Smartphone(Camera, Phone):
        def display(self):
            print("Smartphone Features:")
            self.take_photo()
            self.make_call()

    s = Smartphone()
    s.display()


def inheritance_15():
    print("\n Q15 Person -> Student -> ResearchStudent ")
    inheritance_5()


def inheritance_16():
    print("\n Q16 Person -> Student -> ResearchStudent ")
    inheritance_5()


def inheritance_17():
    print("\n Q17 Animal -> Dog/Cat/Cow")

    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(self.name, "is eating.")

    class Dog(Animal):
        def sound(self):
            print(self.name, "says: Woof!")

    class Cat(Animal):
        def sound(self):
            print(self.name, "says: Meow!")

    class Cow(Animal):
        def sound(self):
            print(self.name, "says: Moo!")

    animals = [
        Dog("Dog"),
        Cat("Cat"),
        Cow("Cow")
    ]

    for animal in animals:
        animal.eat()
        animal.sound()


def inheritance_18():
    print("\n--- Q18 Person -> Doctor/Patient and Multiple Inheritance ---")

    class Person:
        def __init__(self, name):
            self.name = name

    class Doctor(Person):
        def treat(self):
            print(self.name, "is treating patients.")

    class Patient(Person):
        def checkup(self):
            print(self.name, "is undergoing checkup.")

    class Surgeon(Doctor):
        def surgery(self):
            print(self.name, "performs surgery.")

    class MedicalResearcher(Doctor):
        def research(self):
            print(self.name, "does medical research.")

    class SurgeonResearcher(Surgeon, MedicalResearcher):
        def display(self):
            print("Name:", self.name)
            self.treat()
            self.surgery()
            self.research()

    sr = SurgeonResearcher("Dr. Sharma")
    sr.display()

    p = Patient("Rahul")
    p.checkup()


#POLYMORPHISM PROGRAMS

def polymorphism_1():
    print("\n Q1 Shape Area Polymorphism")

    class Shape:
        def area(self):
            pass

    class Circle(Shape):
        def area(self):
            return 3.14 * 5 * 5

    class Rectangle(Shape):
        def area(self):
            return 10 * 5

    class Triangle(Shape):
        def area(self):
            return 0.5 * 10 * 6

    shapes = [Circle(), Rectangle(), Triangle()]

    for shape in shapes:
        print("Area:", shape.area())


def polymorphism_2():
    print("\n Q2 Employee Salary Polymorphism ")

    class Employee:
        def calculate_salary(self):
            return 0

    class Manager(Employee):
        def calculate_salary(self):
            return 70000

    class Developer(Employee):
        def calculate_salary(self):
            return 60000

    class Tester(Employee):
        def calculate_salary(self):
            return 50000

    employees = [Manager(), Developer(), Tester()]

    for employee in employees:
        print("Salary:", employee.calculate_salary())


def polymorphism_3():
    print("\n Q3 Vehicle Start Polymorphism ")

    class Vehicle:
        def start(self):
            print("Vehicle starts.")

    class Car(Vehicle):
        def start(self):
            print("Car starts with key.")

    class Bike(Vehicle):
        def start(self):
            print("Bike starts with self-start.")

    class Bus(Vehicle):
        def start(self):
            print("Bus starts with ignition.")

    vehicles = [Car(), Bike(), Bus()]

    for vehicle in vehicles:
        vehicle.start()


def polymorphism_4():
    print("\n Q4 Animal Sound Polymorphism ")

    class Animal:
        def sound(self):
            print("Animal makes sound.")

    class Dog(Animal):
        def sound(self):
            print("Dog: Woof!")

    class Cat(Animal):
        def sound(self):
            print("Cat: Meow!")

    class Cow(Animal):
        def sound(self):
            print("Cow: Moo!")

    class Lion(Animal):
        def sound(self):
            print("Lion: Roar!")

    animals = [Dog(), Cat(), Cow(), Lion()]

    for animal in animals:
        animal.sound()


def polymorphism_5():
    print("\n Q5 Notification Polymorphism ")

    class Notification:
        def send(self):
            print("Sending notification.")

    class Email(Notification):
        def send(self):
            print("Sending Email.")

    class SMS(Notification):
        def send(self):
            print("Sending SMS.")

    class Push(Notification):
        def send(self):
            print("Sending Push Notification.")

    notifications = [Email(), SMS(), Push()]

    for n in notifications:
        n.send()


def polymorphism_6():
    print("\n Q6 Student Grade Polymorphism ")

    class Student:
        def calculate_grade(self):
            return "Grade calculated"

    class Engineering(Student):
        def calculate_grade(self):
            return "Engineering Grade: A"

    class Medical(Student):
        def calculate_grade(self):
            return "Medical Grade: B"

    class Management(Student):
        def calculate_grade(self):
            return "Management Grade: A"

    students = [Engineering(), Medical(), Management()]

    for student in students:
        print(student.calculate_grade())


def polymorphism_7():
    print("\nQ7 Bank Interest Polymorphism ")

    class BankAccount:
        def calculate_interest(self):
            return 0

    class Savings(BankAccount):
        def calculate_interest(self):
            return 7000

    class Current(BankAccount):
        def calculate_interest(self):
            return 2000

    class FixedDeposit(BankAccount):
        def calculate_interest(self):
            return 10000

    accounts = [Savings(), Current(), FixedDeposit()]

    for account in accounts:
        print("Interest:", account.calculate_interest())


def polymorphism_8():
    print("\n Q8 Report Generation Polymorphism ")

    class Report:
        def generate(self):
            print("Generating report.")

    class PDFReport(Report):
        def generate(self):
            print("Generating PDF Report.")

    class ExcelReport(Report):
        def generate(self):
            print("Generating Excel Report.")

    class HTMLReport(Report):
        def generate(self):
            print("Generating HTML Report.")

    def generate_report(report):
        report.generate()

    generate_report(PDFReport())
    generate_report(ExcelReport())
    generate_report(HTMLReport())


def polymorphism_9():
    print("\n Q9 Distance Operator Overloading ")

    class Distance:
        def __init__(self, feet, inches):
            self.feet = feet
            self.inches = inches

        def __add__(self, other):
            total_inches = (
                self.feet * 12 + self.inches +
                other.feet * 12 + other.inches
            )

            feet = total_inches // 12
            inches = total_inches % 12

            return Distance(feet, inches)

        def display(self):
            print(self.feet, "feet", self.inches, "inches")

    d1 = Distance(5, 8)
    d2 = Distance(3, 6)

    d3 = d1 + d2
    d3.display()


def polymorphism_10():
    print("\n Q10 Student Comparison Operator Overloading ")

    class Student:
        def __init__(self, name, total_marks):
            self.name = name
            self.total_marks = total_marks

        def __gt__(self, other):
            return self.total_marks > other.total_marks

        def __lt__(self, other):
            return self.total_marks < other.total_marks

    s1 = Student("Amit", 450)
    s2 = Student("Rahul", 400)

    print("Amit > Rahul:", s1 > s2)
    print("Amit < Rahul:", s1 < s2)


def polymorphism_11():
    print("\nQ11 Product Comparison Operator Overloading ")

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __eq__(self, other):
            return self.price == other.price

        def __gt__(self, other):
            return self.price > other.price

    p1 = Product("Laptop", 60000)
    p2 = Product("Mobile", 30000)

    print("Same Price:", p1 == p2)
    print("Laptop Costlier:", p1 > p2)


def polymorphism_12():
    print("\n Q12 Payment Polymorphism ")

    class Payment:
        def make_payment(self):
            print("Making payment.")

    class UPIPayment(Payment):
        def make_payment(self):
            print("Payment made using UPI.")

    class CardPayment(Payment):
        def make_payment(self):
            print("Payment made using Card.")

    class WalletPayment(Payment):
        def make_payment(self):
            print("Payment made using Wallet.")

    def process_payment(payment):
        payment.make_payment()

    process_payment(UPIPayment())
    process_payment(CardPayment())
    process_payment(WalletPayment())


def polymorphism_13():
    print("\n Q13 Person Role Polymorphism ")

    class Person:
        def display_role(self):
            print("Person")

    class Student(Person):
        def display_role(self):
            print("Student")

    class Faculty(Person):
        def display_role(self):
            print("Faculty")

    class Administrator(Person):
        def display_role(self):
            print("Administrator")

    people = [Student(), Faculty(), Administrator()]

    for person in people:
        person.display_role()


def polymorphism_14():
    print("\nQ14 Media Play Polymorphism ")

    class Media:
        def play(self):
            print("Playing media.")

    class Audio(Media):
        def play(self):
            print("Playing audio.")

    class Video(Media):
        def play(self):
            print("Playing video.")

    class Podcast(Media):
        def play(self):
            print("Playing podcast.")

    media = [Audio(), Video(), Podcast()]

    for item in media:
        item.play()


def polymorphism_15():
    print("\n Q15 Smart Device Polymorphism ")

    class SmartDevice:
        def turn_on(self):
            print("Device turned on.")

        def turn_off(self):
            print("Device turned off.")

    class Light(SmartDevice):
        def turn_on(self):
            print("Light turned on.")

        def turn_off(self):
            print("Light turned off.")

    class Fan(SmartDevice):
        def turn_on(self):
            print("Fan turned on.")

        def turn_off(self):
            print("Fan turned off.")

    class AC(SmartDevice):
        def turn_on(self):
            print("AC turned on.")

        def turn_off(self):
            print("AC turned off.")

    class TV(SmartDevice):
        def turn_on(self):
            print("TV turned on.")

        def turn_off(self):
            print("TV turned off.")

    devices = [Light(), Fan(), AC(), TV()]

    for device in devices:
        device.turn_on()
        device.turn_off()

# ABSTRACTION PROGRAMS


def abstraction_1():
    print("\nQ1 Abstract Shape")

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Circle(Shape):
        def area(self):
            return 3.14 * 5 * 5

    class Rectangle(Shape):
        def area(self):
            return 10 * 5

    class Triangle(Shape):
        def area(self):
            return 0.5 * 10 * 6

    shapes = [Circle(), Rectangle(), Triangle()]

    for shape in shapes:
        print("Area:", shape.area())


def abstraction_2():
    print("\nQ2 Abstract Vehicle ")

    class Vehicle(ABC):
        @abstractmethod
        def start(self):
            pass

        @abstractmethod
        def stop(self):
            pass

    class Car(Vehicle):
        def start(self):
            print("Car started.")

        def stop(self):
            print("Car stopped.")

    class Bike(Vehicle):
        def start(self):
            print("Bike started.")

        def stop(self):
            print("Bike stopped.")

    class Bus(Vehicle):
        def start(self):
            print("Bus started.")

        def stop(self):
            print("Bus stopped.")

    vehicles = [Car(), Bike(), Bus()]

    for vehicle in vehicles:
        vehicle.start()
        vehicle.stop()


def abstraction_3():
    print("\n Q3 Abstract Bank Account ")

    class BankAccount(ABC):
        @abstractmethod
        def deposit(self, amount):
            pass

        @abstractmethod
        def withdraw(self, amount):
            pass

    class SavingsAccount(BankAccount):
        def __init__(self):
            self.balance = 10000

        def deposit(self, amount):
            self.balance += amount
            print("Savings Balance:", self.balance)

        def withdraw(self, amount):
            self.balance -= amount
            print("Savings Balance:", self.balance)

    class CurrentAccount(BankAccount):
        def __init__(self):
            self.balance = 20000

        def deposit(self, amount):
            self.balance += amount
            print("Current Balance:", self.balance)

        def withdraw(self, amount):
            self.balance -= amount
            print("Current Balance:", self.balance)

    s = SavingsAccount()
    s.deposit(5000)
    s.withdraw(2000)

    c = CurrentAccount()
    c.deposit(5000)
    c.withdraw(3000)


def abstraction_4():
    print("\n Q4 Abstract Food Order ")

    class FoodOrder(ABC):
        @abstractmethod
        def calculate_bill(self):
            pass

        @abstractmethod
        def delivery_charge(self):
            pass

    class RestaurantOrder(FoodOrder):
        def calculate_bill(self):
            return 500

        def delivery_charge(self):
            return 0

    class HomeDeliveryOrder(FoodOrder):
        def calculate_bill(self):
            return 500

        def delivery_charge(self):
            return 50

    orders = [RestaurantOrder(), HomeDeliveryOrder()]

    for order in orders:
        total = order.calculate_bill() + order.delivery_charge()
        print("Total Bill:", total)


def abstraction_5():
    print("\n Q5 Abstract Patient")

    class Patient(ABC):
        @abstractmethod
        def calculate_bill(self):
            pass

        @abstractmethod
        def treatment(self):
            pass

    class InPatient(Patient):
        def calculate_bill(self):
            return 10000

        def treatment(self):
            print("In-patient treatment.")

    class OutPatient(Patient):
        def calculate_bill(self):
            return 3000

        def treatment(self):
            print("Out-patient treatment.")

    class EmergencyPatient(Patient):
        def calculate_bill(self):
            return 15000

        def treatment(self):
            print("Emergency treatment.")

    patients = [
        InPatient(),
        OutPatient(),
        EmergencyPatient()
    ]

    for patient in patients:
        patient.treatment()
        print("Bill:", patient.calculate_bill())


def abstraction_6():
    print("\n Q6 Abstract Transport ")

    class Transport(ABC):
        @abstractmethod
        def calculate_fare(self, distance):
            pass

    class Bus(Transport):
        def calculate_fare(self, distance):
            return distance * 5

    class Train(Transport):
        def calculate_fare(self, distance):
            return distance * 3

    class Taxi(Transport):
        def calculate_fare(self, distance):
            return distance * 15

    class Flight(Transport):
        def calculate_fare(self, distance):
            return distance * 10

    transports = [Bus(), Train(), Taxi(), Flight()]

    for transport in transports:
        print("Fare for 100 km:", transport.calculate_fare(100))


def abstraction_7():
    print("\nQ7 Abstract Question ")

    class Question(ABC):
        @abstractmethod
        def evaluate_answer(self):
            pass

    class MCQ(Question):
        def evaluate_answer(self):
            print("MCQ answer evaluated.")

    class TrueFalse(Question):
        def evaluate_answer(self):
            print("True/False answer evaluated.")

    class Descriptive(Question):
        def evaluate_answer(self):
            print("Descriptive answer evaluated.")

    questions = [MCQ(), TrueFalse(), Descriptive()]

    for question in questions:
        question.evaluate_answer()


def abstraction_8():
    print("\n--- Q8 Abstract Authentication ---")

    class Authentication(ABC):
        @abstractmethod
        def authenticate(self):
            pass

    class Password(Authentication):
        def authenticate(self):
            print("Authenticated using Password.")

    class OTP(Authentication):
        def authenticate(self):
            print("Authenticated using OTP.")

    class Biometric(Authentication):
        def authenticate(self):
            print("Authenticated using Biometric.")

    methods = [Password(), OTP(), Biometric()]

    for method in methods:
        method.authenticate()


def abstraction_9():
    print("\n Q9 Abstract Cloud Storage")

    class CloudStorage(ABC):
        @abstractmethod
        def upload(self):
            pass

        @abstractmethod
        def download(self):
            pass

        @abstractmethod
        def delete(self):
            pass

    class GoogleDrive(CloudStorage):
        def upload(self):
            print("File uploaded to Google Drive.")

        def download(self):
            print("File downloaded from Google Drive.")

        def delete(self):
            print("File deleted from Google Drive.")

    class OneDrive(CloudStorage):
        def upload(self):
            print("File uploaded to OneDrive.")

        def download(self):
            print("File downloaded from OneDrive.")

        def delete(self):
            print("File deleted from OneDrive.")

    class Dropbox(CloudStorage):
        def upload(self):
            print("File uploaded to Dropbox.")

        def download(self):
            print("File downloaded from Dropbox.")

        def delete(self):
            print("File deleted from Dropbox.")

    services = [GoogleDrive(), OneDrive(), Dropbox()]

    for service in services:
        service.upload()
        service.download()
        service.delete()


def abstraction_10():
    print("\n Q10 Abstract Appointment")

    class Appointment(ABC):
        @abstractmethod
        def book_appointment(self):
            pass

        @abstractmethod
        def calculate_fee(self):
            pass

    class GeneralAppointment(Appointment):
        def book_appointment(self):
            print("General appointment booked.")

        def calculate_fee(self):
            return 500

    class SpecialistAppointment(Appointment):
        def book_appointment(self):
            print("Specialist appointment booked.")

        def calculate_fee(self):
            return 1000

    class EmergencyAppointment(Appointment):
        def book_appointment(self):
            print("Emergency appointment booked.")

        def calculate_fee(self):
            return 2000

    appointments = [
        GeneralAppointment(),
        SpecialistAppointment(),
        EmergencyAppointment()
    ]

    for appointment in appointments:
        appointment.book_appointment()
        print("Fee:", appointment.calculate_fee())

#                    PROGRAM DICTIONARIES

inheritance_programs = {
    1: inheritance_1,
    2: inheritance_2,
    3: inheritance_3,
    4: inheritance_4,
    5: inheritance_5,
    6: inheritance_6,
    7: inheritance_7,
    8: inheritance_8,
    9: inheritance_9,
    10: inheritance_10,
    11: inheritance_11,
    12: inheritance_12,
    13: inheritance_13,
    14: inheritance_14,
    15: inheritance_15,
    16: inheritance_16,
    17: inheritance_17,
    18: inheritance_18
}

polymorphism_programs = {
    1: polymorphism_1,
    2: polymorphism_2,
    3: polymorphism_3,
    4: polymorphism_4,
    5: polymorphism_5,
    6: polymorphism_6,
    7: polymorphism_7,
    8: polymorphism_8,
    9: polymorphism_9,
    10: polymorphism_10,
    11: polymorphism_11,
    12: polymorphism_12,
    13: polymorphism_13,
    14: polymorphism_14,
    15: polymorphism_15
}

abstraction_programs = {
    1: abstraction_1,
    2: abstraction_2,
    3: abstraction_3,
    4: abstraction_4,
    5: abstraction_5,
    6: abstraction_6,
    7: abstraction_7,
    8: abstraction_8,
    9: abstraction_9,
    10: abstraction_10
}

#MENU FUNCTIONS

def section_menu(title, programs):
    while True:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)

        for number in programs:
            print(number, ".", "Run Program", number)

        print("0 . Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            break

        if choice.isdigit() and int(choice) in programs:
            number = int(choice)

            print("\n" + "-" * 55)
            print("Running Program", number)
            print("-" * 55)

            programs[number]()

            input("\nPress Enter to continue...")
        else:
            print("Invalid choice. Please try again.")


def run_all_programs():
    print("\n" + "=" * 60)
    print("RUNNING ALL 43 OOP PROGRAMS")
    print("=" * 60)

    print("\n\nINHERITANCE")

    for number, program in inheritance_programs.items():
        print("\n\n" + "#" * 60)
        print("INHERITANCE PROGRAM", number)
        print("#" * 60)
        program()

    print("\n\nPOLYMORPHISM ")

    for number, program in polymorphism_programs.items():
        print("\n\n" + "#" * 60)
        print("POLYMORPHISM PROGRAM", number)
        print("#" * 60)
        program()

    print("\n\nABSTRACTION ")

    for number, program in abstraction_programs.items():
        print("\n\n" + "#" * 60)
        print("ABSTRACTION PROGRAM", number)
        print("#" * 60)
        program()

    print("\n\n" + "=" * 60)
    print("ALL PROGRAMS COMPLETED")
    print("=" * 60)


#MAIN MENU

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("              OOP PROGRAM COLLECTION")
        print("=" * 60)
        print("1. Inheritance")
        print("2. Polymorphism")
        print("3. Abstraction")
        print("4. Run All 43 Programs")
        print("0. Exit")
        print("=" * 60)

        choice = input("Enter your choice: ")

        if choice == "1":
            section_menu(
                "INHERITANCE PROGRAMS",
                inheritance_programs
            )

        elif choice == "2":
            section_menu(
                "POLYMORPHISM PROGRAMS",
                polymorphism_programs
            )

        elif choice == "3":
            section_menu(
                "ABSTRACTION PROGRAMS",
                abstraction_programs
            )

        elif choice == "4":
            run_all_programs()
            input("\nPress Enter to return to main menu...")

        elif choice == "0":
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice. Please enter a valid option.")

#START PROGRAM


if __name__ == "__main__":
    main()