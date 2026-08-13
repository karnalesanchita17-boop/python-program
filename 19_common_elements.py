# 19. Find common elements between two tuples
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

common = ()

for item in t1:
    if item in t2 and item not in common:
        common += (item,)

print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Common elements:", common)
