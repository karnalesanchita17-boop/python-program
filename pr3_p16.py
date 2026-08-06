# Python List Programs 21-30
# 21. Merge two lists
list1=[1, 2, 3]
list2=[4, 5, 6]
merged=list1 + list2
print("21. Merged List:", merged)
# 22. Common elements between two lists
a=[1, 2, 3, 4]
b=[3, 4, 5, 6]
common=[]
for i in a:
    if i in b and i not in common:
        common.append(i)
print("22. Common Elements:", common)
# 23. Frequency of each element
nums = [1,2,2,3,3,3,4]
print("23. Frequency:")
for i in nums:
    if nums.count(i)==1 or i==nums[nums.index(i)]:
        print(i, ":", nums.count(i))
# 24. Rotate list
lst=[10,20,30,40,50]
left=lst[1:]+lst[:1]
right=lst[-1:]+lst[:-1]
print("24. Left Rotate:", left)
print("24. Right Rotate:", right)
# 25. Remove duplicates preserving order
nums=[1,2,2,3,1,4,5,3]
unique=[]
for x in nums:
    if x not in unique:
        unique.append(x)
print("25. Unique:", unique)
# 26. Student marks
marks=[60,70,80,90,55,65,75,85,95,50,68,72,88,91,77,83,59,62,74,81]
highest=max(marks)
lowest=min(marks)
avg=sum(marks)/len(marks)
above=0
below=0
for m in marks:
    if m>avg: above+=1
    elif m<avg: below+=1
print("26. Highest:",highest)
print("Lowest:",lowest)
print("Average:",avg)
print("Above Average:",above)
print("Below Average:",below)

# 27. Employee salaries
sal=[25000,35000,45000,55000,60000,28000,72000]
print("27. Highest:",max(sal))
print("Lowest:",min(sal))
print("Average:",sum(sal)/len(sal))
print("Above 50000:",sum(1 for s in sal if s>50000))
print("Below 30000:",sum(1 for s in sal if s<30000))
# 28. Batsman scores
scores=[45,67,120,89,150,32,100,75,10,56]
print("28. Highest:",max(scores))
print("Lowest:",min(scores))
print("Total Runs:",sum(scores))
print("Average:",sum(scores)/len(scores))
print("Centuries:",sum(1 for s in scores if s>=100))
print("Half-centuries:",sum(1 for s in scores if 50<=s<=99))
# 29. Temperature of 30 days
temps=[30,31,32,33,34,35,36,30,29,28,31,32,33,34,35,36,37,38,39,30,31,32,33,34,35,36,29,28,27,30]
avg=sum(temps)/len(temps)
print("29. Hottest:",max(temps))
print("Coldest:",min(temps))
print("Average:",avg)
print("Above Average:",sum(1 for t in temps if t>avg))
print("Below Average:",sum(1 for t in temps if t<avg))
# 30. Patient records
names=["Amit","Priya","Rahul"]
ages=[25,30,40]
names.append("Sneha")
ages.append(35)
if "Rahul" in names:
    i=names.index("Rahul")
    names.pop(i)
    ages.pop(i)
search="Priya"
print("30. Search:", search in names)
print("Patients:")
for i in range(len(names)):
    print(names[i], "-", ages[i])
print("Total Patients:",len(names))