numbers=[]
for i in range(10):
    num=int(input("Enter number: "))
    numbers.append(num)
ascending=sorted(numbers)
descending=sorted(numbers, reverse=True)
print("Ascending Order:", ascending)
print("Descending Order:", descending)