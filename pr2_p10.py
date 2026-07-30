#program to check the entered number is prime or not
n=int(input("Enter a number: "))
if n<=1:
    print("Not Prime")
else:
    i=2
    prime=True
    while i<n:
        if n%i==0:
            prime=False
            break
        i+=1
    if prime:
        print("Prime")
    else:
        print("Not Prime")