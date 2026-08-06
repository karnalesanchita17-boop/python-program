numbers=[10, 50, 30, 80, 60]
largest=second=numbers[0]
for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print("Largest =", largest)
print("Second Largest =", second)