# 23. Patient records operations
patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 31, "B+"),
    (103, "Amit", 40, "O+"),
    (104, "Sneha", 28, "A+"),
    (105, "Neha", 35, "O+")
)

# Display all records
print("All Patient Records:")
for patient in patients:
    print("ID:", patient[0], "| Name:", patient[1],
          "| Age:", patient[2], "| Blood Group:", patient[3])

# Search patient by ID
search_id = int(input("\nEnter Patient ID to search: "))
found = False

for patient in patients:
    if patient[0] == search_id:
        print("Patient found:", patient)
        found = True
        break

if not found:
    print("Patient not found.")

# Count total patients
print("Total number of patients:", len(patients))

# Display patients with a specific blood group
blood_group = input("Enter blood group to search: ")

print("Patients with blood group", blood_group, ":")
found = False

for patient in patients:
    if patient[3].upper() == blood_group.upper():
        print(patient)
        found = True

if not found:
    print("No patient found with this blood group.")
