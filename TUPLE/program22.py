# Create tuples containing Employee ID, Name and Salary. Display all employee information.
employees = (
    (101, "Rahul", 25000),
    (102, "Sneha", 30000),
    (103, "Amit", 28000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()