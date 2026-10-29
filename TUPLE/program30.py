# Create a tuple containing patient records and perform all operations.
patients = (
    (101, "Pallavi", 20, "A+"),
    (102, "Rahul", 25, "B+"),
    (103, "Sneha", 22, "A+"),
    (104, "Amit", 30, "O+")
)

# Display all records
print("All Patient Records:")
for patient in patients:
    print(patient)

# Search patient by ID
patient_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient Found:")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found")

# Count total patients
print("\nTotal number of patients:", len(patients))

# Display patients with specific blood group
blood_group = input("\nEnter blood group: ")

print("Patients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)