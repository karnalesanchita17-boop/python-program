import numpy as np
#  NUMPY PROGRAMS

def program_1():
    print("\n Q1: One-Dimensional Array ")
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("Array:", arr)
    print("Size:", arr.size)
    print("Data Type:", arr.dtype)
    print("Number of Dimensions:", arr.ndim)

def program_2():
    print("\nQ2: Arithmetic Operations on Two Arrays ")
    a = np.array([10, 20, 30, 40, 50])
    b = np.array([1, 2, 3, 4, 5])
    print("Array A:", a)
    print("Array B:", b)
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Modulus:", a % b)

def program_3():
    print("\n Q3: Maximum, Minimum, Sum and Average ")
    arr = np.array([10, 25, 35, 45, 50, 65, 70, 80, 90, 100])
    print("Array:", arr)
    print("Maximum:", np.max(arr))
    print("Minimum:", np.min(arr))
    print("Sum:", np.sum(arr))
    print("Average:", np.mean(arr))

def program_4():
    print("\n Q4: Even and Odd Numbers Using Boolean Indexing ")
    arr = np.arange(1, 21)
    even = arr[arr % 2 == 0]
    odd = arr[arr % 2 != 0]
    print("Array:", arr)
    print("Even Numbers:", even)
    print("Odd Numbers:", odd)

def program_5():
    print("\n Q5: Reshaping 1D Array ")
    arr = np.arange(1, 13)
    print("Original Array:")
    print(arr)
    print("\n2 x 6 Matrix:")
    print(arr.reshape(2, 6))
    print("\n3 x 4 Matrix:")
    print(arr.reshape(3, 4))
    print("\n4 x 3 Matrix:")
    print(arr.reshape(4, 3))

def program_6():
    print("\nQ6: Matrix Addition ")
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    b = np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])
    print("Matrix A:")
    print(a)
    print("\nMatrix B:")
    print(b)
    print("\nMatrix Addition:")
    print(a + b)

def program_7():
    print("\n Q7: Matrix Multiplication ")
    a = np.array([
        [1, 2],
        [3, 4]
    ])
    b = np.array([
        [5, 6],
        [7, 8]
    ])
    print("Matrix A:")
    print(a)
    print("\nMatrix B:")
    print(b)
    result = np.matmul(a, b)
    print("\nMatrix Multiplication:")
    print(result)

def program_8():
    print("\n Q8: Transpose of 3 x 4 Matrix ")
    matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print("Original Matrix:")
    print(matrix)
    print("\nTranspose:")
    print(matrix.T)

def program_9():
    print("\n Q9: Accessing Elements of 4 x 4 Matrix ")
    matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    print("Matrix:")
    print(matrix)
    print("\nFirst Row:")
    print(matrix[0])
    print("\nLast Column:")
    print(matrix[:, -1])
    print("\nDiagonal Elements:")
    print(np.diag(matrix))
    print("\nSecond and Third Rows:")
    print(matrix[1:3])

def program_10():
    print("\n Q10: Row and Column Sums ")
    matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    print("Matrix:")
    print(matrix)
    print("\nSum of Each Row:")
    print(np.sum(matrix, axis=1))
    print("\nSum of Each Column:")
    print(np.sum(matrix, axis=0))

def program_11():
    print("\n Q11: Array Slicing ")
    arr = np.arange(1, 21)
    print("Array:")
    print(arr)
    print("\nFirst 5 Elements:")
    print(arr[:5])
    print("\nLast 5 Elements:")
    print(arr[-5:])
    print("\nAlternate Elements:")
    print(arr[::2])
    print("\nReverse Order:")
    print(arr[::-1])

def program_12():
    print("\n- Q12: Replace Values Greater Than 50 ")
    arr = np.array([10, 25, 55, 40, 75, 60, 30, 90, 45, 80])
    print("Original Array:")
    print(arr)
    arr[arr > 50] = 0
    print("\nArray After Replacement:")
    print(arr)

def program_13():
    print("\n Q13: Sorting Array ")
    arr = np.array([45, 12, 89, 23, 67, 5, 34, 90])
    print("Original Array:")
    print(arr)
    print("\nAscending Order:")
    print(np.sort(arr))
    print("\nDescending Order:")
    print(np.sort(arr)[::-1])

def program_14():
    print("\n Q14: Unique Elements ")
    arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40, 50])
    print("Original Array:")
    print(arr)
    print("\nUnique Elements:")
    print(np.unique(arr))

def program_15():
    print("\n Q15: Horizontal and Vertical Concatenation ")
    a = np.array([
        [1, 2],
        [3, 4]
    ])
    b = np.array([
        [5, 6],
        [7, 8]
    ])
    print("Array A:")
    print(a)
    print("\nArray B:")
    print(b)
    print("\nHorizontal Concatenation:")
    print(np.hstack((a, b)))
    print("\nVertical Concatenation:")
    print(np.vstack((a, b)))

def program_16():
    print("\n Q16: Student Marks Statistics ")
    marks = np.array([
        85, 72, 90, 65, 78,
        88, 95, 60, 75, 82
    ])
    print("Marks:", marks)
    print("Highest Marks:", np.max(marks))
    print("Lowest Marks:", np.min(marks))
    print("Average Marks:", np.mean(marks))
    print("Median:", np.median(marks))
    print("Standard Deviation:", np.std(marks))

def program_17():
    print("\n Q17: Students Above Class Average ")
    marks = np.array([
        45, 67, 89, 76, 55,
        92, 81, 63, 70, 88,
        49, 95, 73, 60, 85,
        78, 52, 91, 68, 80
    ])
    average = np.mean(marks)
    above_average = marks[marks > average]
    print("Marks:")
    print(marks)
    print("\nClass Average:", average)
    print("\nStudents Scoring Above Average:")
    print(above_average)

def program_18():
    print("\n Q18: 3D Array Shape (2, 3, 4) ")
    arr = np.arange(1, 25).reshape(2, 3, 4)
    print("3D Array:")
    print(arr)
    print("\nNumber of Dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Size:", arr.size)

def program_19():
    print("\n Q19: Accessing Elements of 3D Array ")
    arr = np.arange(1, 25).reshape(2, 3, 4)
    print("3D Array:")
    print(arr)
    print("\nFirst Element:")
    print(arr[0, 0, 0])
    print("\nLast Element:")
    print(arr[-1, -1, -1])
    print("\nElement at Index [0,1,2]:")
    print(arr[0, 1, 2])
    print("\nElement at Index [1,2,3]:")
    print(arr[1, 2, 3])

def program_20():
    print("\n Q20: Sum Operations on 3D Array ")
    arr = np.arange(1, 25).reshape(2, 3, 4)
    print("3D Array:")
    print(arr)
    print("\nSum of All Elements:")
    print(np.sum(arr))
    print("\nSum of Each Layer:")
    print(np.sum(arr, axis=(1, 2)))
    print("\nSum Along Rows:")
    print(np.sum(arr, axis=2))
    print("\nSum Along Columns:")
    print(np.sum(arr, axis=1))

def program_21():
    print("\n- Q21: Replace 3D Values Greater Than 50 ")
    np.random.seed(10)
    arr = np.random.randint(1, 101, size=(2, 3, 4))
    print("Original 3D Array:")
    print(arr)
    arr[arr > 50] = 0
    print("\nAfter Replacing Values Greater Than 50:")
    print(arr)

def program_22():
    print("\n Q22: Statistics of Random 3D Array ")
    np.random.seed(10)
    arr = np.random.randint(1, 101, size=(3, 4, 5))
    print("3D Array:")
    print(arr)
    print("\nMean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Variance:", np.var(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))

def program_23():
    print("\n Q23: Flatten 3D Array ")
    arr = np.arange(1, 25).reshape(2, 3, 4)
    print("Original 3D Array:")
    print(arr)
    flattened = arr.flatten()
    print("\nFlattened Array:")
    print(flattened)


def program_24():
    print("\n Q24: Flatten 3D Array and Statistics ")
    arr = np.arange(1, 28).reshape(3, 3, 3)
    print("Original 3D Array:")
    print(arr)
    flattened = arr.flatten()
    print("\nFlattened Array:")
    print(flattened)
    print("\nSum:", np.sum(flattened))
    print("Average:", np.mean(flattened))
    print("Maximum:", np.max(flattened))
    print("Minimum:", np.min(flattened))


def program_25():
    print("\n Q25: Filtering Flattened 3D Array ")
    np.random.seed(10)
    arr = np.random.randint(1, 101, size=(3, 4, 5))
    print("Original 3D Array:")
    print(arr)
    flattened = arr.flatten()
    average = np.mean(flattened)
    print("\nFlattened Array:")
    print(flattened)
    print("\nElements Greater Than 50:")
    print(flattened[flattened > 50])
    print("\nEven Numbers:")
    print(flattened[flattened % 2 == 0])
    print("\nAverage:", average)
    print("\nElements Less Than Average:")
    print(flattened[flattened < average])

# PROGRAM DICTIONARY

programs = {
    1: program_1,
    2: program_2,
    3: program_3,
    4: program_4,
    5: program_5,
    6: program_6,
    7: program_7,
    8: program_8,
    9: program_9,
    10: program_10,
    11: program_11,
    12: program_12,
    13: program_13,
    14: program_14,
    15: program_15,
    16: program_16,
    17: program_17,
    18: program_18,
    19: program_19,
    20: program_20,
    21: program_21,
    22: program_22,
    23: program_23,
    24: program_24,
    25: program_25
}

#RUN ALL PROGRAMS
def run_all():
    print("RUNNING ALL 25 NUMPY PROGRAMS")
    for number, program in programs.items():
        print("\n\n")
        print("#" * 55)
        print(" NUMPY PROGRAM", number)
        print("#" * 55)
        program()
        input("\nPress Enter to run the next program...")
    print(" ALL 25 PROGRAMS COMPLETED")

# MAIN MENU
def main():
    while True:
        print("\n")
        print("=" * 55)
        print(" NUMPY PROGRAMS")
        print("=" * 55)
        print("1. Run Program 1")
        print("2. Run Program 2")
        print("3. Run Program 3")
        print("4. Run Program 4")
        print("5. Run Program 5")
        print("6. Run Program 6")
        print("7. Run Program 7")
        print("8. Run Program 8")
        print("9. Run Program 9")
        print("10. Run Program 10")
        print("11. Run Program 11")
        print("12. Run Program 12")
        print("13. Run Program 13")
        print("14. Run Program 14")
        print("15. Run Program 15")
        print("16. Run Program 16")
        print("17. Run Program 17")
        print("18. Run Program 18")
        print("19. Run Program 19")
        print("20. Run Program 20")
        print("21. Run Program 21")
        print("22. Run Program 22")
        print("23. Run Program 23")
        print("24. Run Program 24")
        print("25. Run Program 25")
        print("26. Run All 25 Programs")
        print("0. Exit")
        print("=" * 55)
        choice = input("Enter your choice: ")
        if choice == "0":
            print("\nThank you!")
            break
        elif choice == "26":
            run_all()
            input("\nPress Enter to return to the main menu...")
        elif choice.isdigit() and int(choice) in programs:
            number = int(choice)
            print("\n" + "-" * 55)
            print("Running NumPy Program", number)
            print("-" * 55)
            programs[number]()
            input("\nPress Enter to return to the main menu...")
        else:
            print("\nInvalid choice. Please try again.")

#START PROGRAM
if __name__ == "__main__":
    main()