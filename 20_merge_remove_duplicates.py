# 20. Merge two tuples and remove duplicates
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

merged = t1 + t2
result = ()

for item in merged:
    if item not in result:
        result += (item,)

print("Merged tuple:", merged)
print("After removing duplicates:", result)
