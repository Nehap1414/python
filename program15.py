
# Create a nested tuple containing student details and display each record.
students = (
    (1, "Pallavi", 85),
    (2, "Rahul", 90),
    (3, "Sneha", 88)
)

for student in students:
    print("Roll No:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])
    print()