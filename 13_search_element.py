# 13. Search for a number in a tuple
numbers = (10, 20, 30, 40, 50)

num = int(input("Enter a number to search: "))

if num in numbers:
    print(num, "exists in the tuple.")
else:
    print(num, "does not exist in the tuple.")
