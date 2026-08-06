cities = ["Mumbai", "Pune", "Kolhapur", "Delhi", "Chennai"]
city = input("Enter city name: ")
if city in cities:
    print(city, "is present in the list.")
else:
    print(city, "is not present in the list.")