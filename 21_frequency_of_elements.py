# 21. Count frequency of each element in a tuple
t = (1, 2, 2, 3, 1, 4, 2, 3, 3, 5)

frequency = {}

for item in t:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Tuple:", t)
print("Frequency of each element:")
for item, count in frequency.items():
    print(item, ":", count)
