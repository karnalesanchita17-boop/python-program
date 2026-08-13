#Python program to create a tuple of five integers and display it.
t=(1,2,3,5,7,11,13)
print("1st ")
print(t)
#program to display 1t, 3rd,last city from tuple containing five city names
t1=("Mumbai","Kolhapur","Pune","Satara","Sangli")
print("\n2nd : ")
print("First city:",t1[0])
print("Last city: ",t1[4])
print("Third city: ",t1[2])
#program to Create a tuple of student names and display the total number of students using the len() function.
t2=("ram","Shyam","Sita","Gita","Riya")
print("\n3rd :")
print("total no. of students =",len(t2))
#Create a tuple of colors. Check whether a given color exists in the tuple
t3=("red","blue","green","orange","yellow")
print("\n4th :")
color=input("Enter color :").lower()
for i in t3:
    if(i==color):
        print(color,"color exist in touple")
    else:
        print(color,"color does not exist in touple")
    break
# program to Create a tuple of fruits and display each fruit using a loop.
fruit=("Mango","Guava","Apple","Banana","Watermelon")
print("\n5th : ")
a=len(fruit)
for i in range(0,a):
    print(fruit[i])
# program to Create a tuple with repeated numbers and count how many times a particular number appears.
num=(1,2,2,1,3,4,5,4,6,8,4,9)
a1=len(num)
n=int(input("\nEnter number: "))
print(n,"appears",num.count(n),"times")
#program to Create a tuple of employee IDs and find the index of a given ID.    
employee_ids=(101,102,103,104,105)
id=int(input("\nEnter employee ID: "))
if id in employee_ids:
    print("Index of employee ID:", employee_ids.index(id))
else:
    print("Employee ID not found")
