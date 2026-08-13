# 22. Convert tuple into sorted tuples
t = (50, 20, 10, 40, 30)

ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))

print("Original tuple:", t)
print("Ascending tuple:", ascending)
print("Descending tuple:", descending)
