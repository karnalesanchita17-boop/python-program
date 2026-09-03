import os
import string

# 1. Create student.txt and write student information
def create_student_file():
    with open("student.txt", "w") as file:
        file.write("Name: Sanchita\n")
        file.write("Roll Number: 101\n")
        file.write("Branch: Computer Science Engineering\n")
        file.write("Semester: 5\n")

    print("student.txt created successfully.")

# 2. Display complete contents of a text file
def display_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            print("\n--- File Contents ---")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")

# 3. Append additional student information
def append_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "a") as file:
            name = input("Enter additional student name: ")
            roll = input("Enter roll number: ")
            branch = input("Enter branch: ")
            file.write("\nName: " + name)
            file.write("\nRoll Number: " + roll)
            file.write("\nBranch: " + branch)
        print("Information appended successfully.")
    except FileNotFoundError:
        print("File not found.")

# 4. Read file line by line
def read_line_by_line():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            print("\n--- Lines ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

# 5. Count total number of lines
def count_lines():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        print("Total number of lines:", len(lines))
    except FileNotFoundError:
        print("File not found.")

# 6. Count total number of words
def count_words():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read()
        words = text.split()
        print("Total number of words:", len(words))
    except FileNotFoundError:
        print("File not found.")

# 7. Count total number of characters including spaces
def count_characters():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read()
        print("Total number of characters:", len(text))
    except FileNotFoundError:
        print("File not found.")

# 8. Display lines in reverse order
def reverse_lines():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        print("\n--- Reverse Order ---")
        for line in reversed(lines):
            print(line.strip())
    except FileNotFoundError:
        print("File not found.")

# 9. Count vowels and consonants
def vowels_consonants():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read()
        vowels = 0
        consonants = 0
        for ch in text.lower():
            if ch.isalpha():
                if ch in "aeiou":
                    vowels += 1
                else:
                    consonants += 1
        print("Vowels:", vowels)
        print("Consonants:", consonants)
    except FileNotFoundError:
        print("File not found.")

# 10. Count alphabets, digits, spaces and special characters
def count_char_types():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read()

        alphabets = 0
        digits = 0
        spaces = 0
        special = 0
        for ch in text:
            if ch.isalpha():
                alphabets += 1
            elif ch.isdigit():
                digits += 1
            elif ch.isspace():
                spaces += 1
            else:
                special += 1
        print("Alphabets:", alphabets)
        print("Digits:", digits)
        print("Spaces:", spaces)
        print("Special characters:", special)
    except FileNotFoundError:
        print("File not found.")

# 11. Find longest word
def longest_word():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read()

        words = text.split()
        if words:
            longest = max(words, key=len)
            print("Longest word:", longest)
            print("Length:", len(longest))
        else:
            print("File is empty.")
    except FileNotFoundError:
        print("File not found.")

# 12. Count frequency of each word using dictionary
def word_frequency():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
        words = text.split()
        frequency = {}
        for word in words:
            word = word.strip(string.punctuation)
            if word:
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1
        print("\n--- Word Frequency ---")
        print(frequency)
    except FileNotFoundError:
        print("File not found.")

# 13. Search word and display occurrences and line numbers
def search_word():
    filename = input("Enter file name: ")
    search = input("Enter word to search: ").lower()
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        count = 0
        line_numbers = []
        for i, line in enumerate(lines, start=1):
            words = line.lower().split()
            line_count = 0
            for word in words:
                word = word.strip(string.punctuation)
                if word == search:
                    count += 1
                    line_count += 1
            if line_count > 0:
                line_numbers.append(i)
        print("Number of occurrences:", count)
        if line_numbers:
            print("Line numbers:", line_numbers)
        else:
            print("Word not found.")
    except FileNotFoundError:
        print("File not found.")


# 14. Replace a word and save modified text
def replace_word():
    filename = input("Enter file name: ")
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")
    try:
        with open(filename, "r") as file:
            text = file.read()
        text = text.replace(old_word, new_word)
        output = input(
            "Enter output file name "
            "(press Enter to use same file): "
        )
        if output == "":
            output = filename
        with open(output, "w") as file:
            file.write(text)
        print("Word replaced successfully.")
    except FileNotFoundError:
        print("File not found.")

# 15. Remove single-line comments from Python source file
def remove_comments():
    filename = input("Enter Python source file: ")
    output = input("Enter output file name: ")
    try:
        with open(filename, "r") as source:
            lines = source.readlines()
        with open(output, "w") as destination:
            for line in lines:
                stripped = line.lstrip()
                if not stripped.startswith("#"):
                    destination.write(line)
        print("Comments removed successfully.")
    except FileNotFoundError:
        print("File not found.")

# 16. Create another file containing text in uppercase
def uppercase_file():
    filename = input("Enter input file name: ")
    output = input("Enter output file name: ")
    try:
        with open(filename, "r") as file:
            text = file.read()
        with open(output, "w") as file:
            file.write(text.upper())
        print("Uppercase file created successfully.")
    except FileNotFoundError:
        print("File not found.")

# 17. Student records
def student_records():
    filename = "students.csv"
    # Create sample file if it does not exist
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("RollNo,Name,Marks\n")
            file.write("101,Amit,85\n")
            file.write("102,Priya,92\n")
            file.write("103,Rahul,78\n")
    students = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            roll, name, marks = line.strip().split(",")
            students.append(
                (roll, name, float(marks))
            )
    print("\n--- All Student Records ---")
    for student in students:
        print(student)
    highest = max(students, key=lambda x: x[2])
    print("\nHighest Marks:")
    print(highest)
    average = sum(s[2] for s in students) / len(students)
    print("Average Marks:", average)
    print("\nStudents scoring more than 80:")
    for student in students:
        if student[2] > 80:
            print(student)

# 18. Employee records
def employee_records():
    filename = "employees.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("101,Amit,IT,50000\n")
            file.write("102,Priya,HR,60000\n")
            file.write("103,Rahul,Finance,55000\n")
    employees = []
    with open(filename, "r") as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append(
                (emp_id, name, dept, float(salary))
            )
    print("\n--- All Employees ---")
    for emp in employees:
        print(emp)
    highest = max(employees, key=lambda x: x[3])
    print("\nHighest-paid employee:")
    print(highest)
    average = sum(e[3] for e in employees) / len(employees)
    print("Average Salary:", average)
    amount = float(input("\nEnter salary amount: "))
    print("\nEmployees earning above", amount)
    for emp in employees:
        if emp[3] > amount:
            print(emp)

# 19. Student attendance
def attendance():
    filename = "attendance.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("101,Amit,80,100\n")
            file.write("102,Priya,70,100\n")
            file.write("103,Rahul,90,100\n")
    print("\n--- Attendance Below 75% ---")
    with open(filename, "r") as file:
        for line in file:
            roll, name, present, total = line.strip().split(",")
            percentage = (
                int(present) / int(total)
            ) * 100
            print(
                roll, name,
                "Attendance:",
                percentage, "%"
            )
            if percentage < 75:
                print("Below 75%")

# 20. Deposits and withdrawals
def bank_transactions():
    filename = "transactions.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("D,5000\n")
            file.write("W,1000\n")
            file.write("D,3000\n")
            file.write("W,500\n")
    total_deposits = 0
    total_withdrawals = 0
    transactions = []
    with open(filename, "r") as file:
        for line in file:
            transaction, amount = line.strip().split(",")
            amount = float(amount)
            transactions.append(amount)
            if transaction == "D":
                total_deposits += amount
            elif transaction == "W":
                total_withdrawals += amount
    final_balance = (
        total_deposits - total_withdrawals
    )
    largest = max(transactions)
    print("Total Deposits:", total_deposits)
    print("Total Withdrawals:", total_withdrawals)
    print("Final Balance:", final_balance)
    print("Largest Transaction:", largest)

# 21. Book management system
def book_management():
    filename = "books.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("101,Python Programming,Guido van Rossum,Available\n")
            file.write("102,Java Programming,James Gosling,Available\n")
    while True:
        print("\n--- BOOK MANAGEMENT ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Available Books")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            with open(filename, "a") as file:
                file.write(
                    book_id + "," +
                    title + "," +
                    author + ",Available\n"
                )
            print("Book added successfully.")
        elif choice == "2":
            search = input("Enter Book ID or Title: ").lower()
            with open(filename, "r") as file:
                found = False
                for line in file:
                    if search in line.lower():
                        print(line.strip())
                        found = True
                if not found:
                    print("Book not found.")
        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            with open(filename, "r") as file:
                lines = file.readlines()
            with open(filename, "w") as file:
                for line in lines:
                    data = line.strip().split(",")
                    if data[0] == book_id:
                        data[3] = "Issued"
                    file.write(",".join(data) + "\n")
            print("Book issued.")
        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            with open(filename, "r") as file:
                lines = file.readlines()
            with open(filename, "w") as file:
                for line in lines:
                    data = line.strip().split(",")
                    if data[0] == book_id:
                        data[3] = "Available"
                    file.write(",".join(data) + "\n")
            print("Book returned.")
        elif choice == "5":
            print("\n--- Available Books ---")
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if data[3] == "Available":
                        print(line.strip())
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

# 22. Combine two text files
def combine_files():
    file1 = input("Enter first file name: ")
    file2 = input("Enter second file name: ")
    output = input("Enter third file name: ")
    try:
        with open(file1, "r") as f1:
            text1 = f1.read()
        with open(file2, "r") as f2:
            text2 = f2.read()
        with open(output, "w") as f3:
            f3.write(text1)
            f3.write("\n")
            f3.write(text2)
        print("Files combined successfully.")
    except FileNotFoundError:
        print("One or more files not found.")

# 23. Compare two text files
def compare_files():
    file1 = input("Enter first file name: ")
    file2 = input("Enter second file name: ")
    try:
        with open(file1, "r") as f1:
            lines1 = f1.readlines()
        with open(file2, "r") as f2:
            lines2 = f2.readlines()
        if lines1 == lines2:
            print("Both files have identical contents.")
        else:
            print("Files are different.")
            minimum = min(len(lines1), len(lines2))
            for i in range(minimum):
                if lines1[i] != lines2[i]:
                    print("First difference is at line:", i + 1)
                    print("File 1:", lines1[i].strip())
                    print("File 2:", lines2[i].strip())
                    break
            else:
                print(
                    "Difference is due to different number of lines."
                )
    except FileNotFoundError:
        print("One or both files not found.")

# MAIN MENU
while True:
    print("       PYTHON FILE HANDLING PROGRAMS")
    print("1.  Create student.txt")
    print("2.  Display complete file")
    print("3.  Append student information")
    print("4.  Read file line by line")
    print("5.  Count lines")
    print("6.  Count words")
    print("7.  Count characters")
    print("8.  Display lines in reverse")
    print("9.  Count vowels and consonants")
    print("10. Count alphabets, digits, spaces, special characters")
    print("11. Find longest word")
    print("12. Word frequency using dictionary")
    print("13. Search word and line numbers")
    print("14. Replace word")
    print("15. Remove Python comments")
    print("16. Convert file to uppercase")
    print("17. Student records")
    print("18. Employee records")
    print("19. Student attendance")
    print("20. Bank transactions")
    print("21. Book management")
    print("22. Combine two files")
    print("23. Compare two files")
    print("0.  Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create_student_file()

    elif choice == "2":
        display_file()

    elif choice == "3":
        append_file()

    elif choice == "4":
        read_line_by_line()

    elif choice == "5":
        count_lines()

    elif choice == "6":
        count_words()

    elif choice == "7":
        count_characters()

    elif choice == "8":
        reverse_lines()

    elif choice == "9":
        vowels_consonants()

    elif choice == "10":
        count_char_types()

    elif choice == "11":
        longest_word()

    elif choice == "12":
        word_frequency()

    elif choice == "13":
        search_word()

    elif choice == "14":
        replace_word()

    elif choice == "15":
        remove_comments()

    elif choice == "16":
        uppercase_file()

    elif choice == "17":
        student_records()

    elif choice == "18":
        employee_records()

    elif choice == "19":
        attendance()

    elif choice == "20":
        bank_transactions()

    elif choice == "21":
        book_management()

    elif choice == "22":
        combine_files()

    elif choice == "23":
        compare_files()

    elif choice == "0":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")

3