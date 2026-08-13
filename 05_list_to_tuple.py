# 5. Accept five numbers in a list and convert to tuple
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

t = tuple(numbers)
print("List:", numbers)
print("Tuple:", t)
