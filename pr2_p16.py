# Program to find the smallest among n numbers
n = int(input("Enter how many numbers: "))
smallest=float('inf')
i=1
while i<=n:
    num=int(input("Enter number: "))
    if num<smallest:
        smallest=num
    i+=1
print("Smallest number =", smallest)