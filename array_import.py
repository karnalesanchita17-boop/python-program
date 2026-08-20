from array import array
import tempfile
import os

# Create an integer array
arr = array('i', [10, 20, 30, 20, 40])
print("Original array:", arr)

# 1. append()
print("\n#1:")
arr.append(50)
print("After append():", arr)

# 2. buffer_info()
print("\n#2:")
print("buffer_info():", arr.buffer_info())

# 3. byteswap()
print("\n#3:",end="")
arr.byteswap()
print("After byteswap():", arr)
# Swap back so remaining operations work normally
arr.byteswap()

# 4. count()
print("\n#4")
print("count(20):", arr.count(20))

# 5. extend()
print("\n#5:")
arr.extend([60, 70])
print("After extend():", arr)

# 6. frombytes()
print("\n#6:")
byte_arr = array('i')
byte_arr.frombytes(array('i', [80, 90]).tobytes())
print("After frombytes():", byte_arr)

# 7. fromfile()
print("\n#7:")
file_arr = array('i', [100, 110])

with tempfile.NamedTemporaryFile(delete=False) as f:
    filename = f.name
    file_arr.tofile(f)

new_arr = array('i')
with open(filename, 'rb') as f:
    new_arr.fromfile(f, 2)

print("After fromfile():", new_arr)
os.remove(filename)

# 8. fromlist()
print("\n#8:")
arr.fromlist([80, 90])
print("After fromlist():", arr)

# 9. fromunicode()
print("\n#9:",)
unicode_arr = array('u')
unicode_arr.fromunicode("Hello")
print("After fromunicode():", unicode_arr)

# 10. index()
print("\n#10:")
print("index(30):",arr.index(30))

# 11. insert()
print("\n#11:")
arr.insert(2,25)
print("After insert():",arr)

# 12. pop()
print("#\n12:")
value=arr.pop()
print("Popped value:",value)
print("After pop():",arr)

# 13. remove()
print("\n#13:")
arr.remove(20)
print("After remove(20):", arr)

# 14. reverse()print("#1",endl="")
print("\n#14:")
arr.reverse()
print("After reverse():",arr)

# 15. tobytes()
print("\n#15:")
b=arr.tobytes()
print("tobytes():",b)

# 16. tofile()
print("\n#16:")
with tempfile.NamedTemporaryFile(delete=False) as f:
    filename=f.name
    arr.tofile(f)

print("tofile(): Data written to file")

# 17. tolist()
print("\n#17:")
list_data=arr.tolist()
print("tolist():",list_data)

# 18. tounicode()
print("\n#18:")
print("tounicode():",unicode_arr.tounicode())