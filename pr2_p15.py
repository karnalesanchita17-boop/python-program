# Program to find the largest among n numbers
n=int(input("Enter how many numbers: "))
largest=float('-inf')
i=1
while i<=n:
    num=int(input("Enter number: "))
    if num>largest:
        largest=num
    i+=1
print("Largest number =", largest)