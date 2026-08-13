# 10. Largest and smallest without max() and min()
numbers = (45, 12, 78, 23, 9, 56, 34)

largest = numbers[0]
smallest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Tuple:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
