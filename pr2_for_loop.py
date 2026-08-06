
# 1. Print natural numbers up to n
n = int(input("Enter n: "))
print("Natural numbers:")
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")

# 2. Print even numbers up to n
n = int(input("Enter n: "))
print("Even numbers:")
for i in range(2, n + 1, 2):
    print(i, end=" ")
print("\n")

# 3. Print odd numbers up to n
n = int(input("Enter n: "))
print("Odd numbers:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print("\n")

# 4. Print series: 1 2 4 8 16 ... up to n terms
n = int(input("Enter number of terms: "))
print("Series:")
term = 1
for i in range(n):
    print(term, end=" ")
    term *= 2
print("\n")

# 5. Alphabet Triangle
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# 6. Reverse Alphabet Triangle
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# 7. Number Triangle
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 8. Repeated Number Triangle
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# 9. Sum of Series:
n = int(input("Enter n: "))
fact = 1
sum_series = 1

for i in range(1, n + 1):
    fact *= i
    sum_series += 1 / fact

print("Sum =", sum_series)
n = int(input("Enter highest even power: "))
x = float(input("Enter x (in radians): "))
fact = 1
cos = 1
for i in range(1, n + 1):
    fact *= i
    if i % 2 == 0:
        term = (x ** i) / fact
        if (i // 2) % 2 == 1:
            cos -= term
        else:
            cos += term

print("Cosine value =", cos)

# 11. Check whether square root is prime
import math
num = int(input("Enter number: "))
root = math.sqrt(num)
if root.is_integer():
    root = int(root)
    if root < 2:
        print("Square root is not prime")
    else:
        prime = True
        for i in range(2, int(root ** 0.5) + 1):
            if root % i == 0:
                prime = False
                break

        if prime:
            print("Square root is prime")
        else:
            print("Square root is not prime")
else:
    print("Square root is not an integer")

# 12. Print ABC pattern
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()