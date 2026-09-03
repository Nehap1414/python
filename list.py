#1)Create a list of five fruits
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print("Fruits:", fruits)
#2)Display first, last and third element
numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])
#3)Replace the third color
colors = ["Red", "Blue", "Green", "Yellow", "Black"]

colors[2] = "Orange"

print("Updated list:", colors)
#4)Add elements at end, beginning and specified position
numbers = [10, 20, 30]

numbers.append(40)       # Add at end
numbers.insert(0, 5)     # Add at beginning
numbers.insert(2, 15)    # Add at specified position

print("Updated list:", numbers)
#4)Remove first, last and specific student
students = ["Aisha", "Rahul", "Sneha", "Aman", "Priya"]

students.pop(0)          # Remove first student
students.pop()           # Remove last student
students.remove("Sneha") # Remove specific student

print("Remaining students:", students)
#5)Find largest and smallest without max() or min()
numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
#7. Accept 10 numbers and calculate sum and average
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
#8. Count even and odd numbersnumbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 11, 22, 33, 44, 55, 66]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
#9. Check whether city exists
cities = ["Kolhapur", "Pune", "Mumbai", "Delhi", "Goa"]

city = input("Enter city name: ")

if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")
#10. Reverse a list without reverse()
numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)
#11. List slicing operations
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])
#12. Elements at even index positions
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Elements at even index positions:")

for i in range(0, len(numbers), 2):
    print(numbers[i])
#13. Sort 10 numbers ascending and descending
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)
#14. Display only unique elements
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)
#15. Find second largest element
numbers = [10, 50, 30, 80, 60, 80]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()

print("Second largest element:", unique[-2])
#16. Nested list for student details
students = [
    ["Aisha", 1, 85],
    ["Rahul", 2, 78],
    ["Sneha", 3, 92],
    ["Aman", 4, 88]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
#17. Addition of two 3 × 3 matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix Addition:")

for row in result:
    print(row)
#18. Shopping cart operations
cart = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display cart")
    print("5. Count total items")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        cart.append(item)
        print("Item added.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print("Item found.")
        else:
            print("Item not found.")

    elif choice == 4:
        print("Shopping cart:", cart)

    elif choice == 5:
        print("Total items:", len(cart))

    elif choice == 6:
        break

    else:
        print("Invalid choice.")
#19. Student attendance management
students = ["Aisha", "Rahul", "Sneha", "Aman"]

print("Total students:", len(students))

name = input("Search student: ")

if name in students:
    print("Student is present.")
else:
    print("Student is absent.")

new_student = input("Enter new student name: ")
students.append(new_student)

absent = input("Enter absent student name to remove: ")

if absent in students:
    students.remove(absent)

print("Updated student list:", students)
#20. Book management
books = ["Python", "Java", "C++"]

# Add book
new_book = input("Enter new book: ")
books.append(new_book)

# Search book
search = input("Enter book to search: ")

if search in books:
    print("Book found.")
else:
    print("Book not found.")

# Remove book
remove = input("Enter book to remove: ")

if remove in books:
    books.remove(remove)
    print("Book removed.")


print("All books:", books)


print("Total books:", len(books))
#21. Merge two lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]

merged = list1 + list2

print("List 1:", list1)
print("List 2:", list2)
print("Merged list:", merged)
#22. Find common elements between two lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)
#23. Count frequency of each element
numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements:")

for key, value in frequency.items():
    print(key, ":", value)
#24. Rotate list left and right by one position
numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Original list:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)
#25. Remove duplicates while preserving original order
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Original list:", numbers)
print("After removing duplicates:", result)
#26. Marks of 20 students
marks = [
    85, 72, 90, 65, 78,
    88, 92, 70, 81, 76,
    95, 68, 84, 79, 73,
    89, 91, 67, 75, 86
]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above)
print("Students below average:", below)
#27. Employee salaries
salaries = [25000, 45000, 60000, 75000, 28000, 52000, 35000, 90000]

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)
#28. Batsman's scores in 10 matches
scores = [45, 120, 75, 30, 100, 55, 80, 150, 25, 65]

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)
#29. Temperature of 30 days
temperature = [
    28, 30, 32, 29, 35, 31, 33, 27, 26, 34,
    36, 30, 29, 31, 37, 28, 32, 35, 33, 30,
    27, 29, 34, 36, 31, 28, 30, 32, 38, 29
]

hottest = max(temperature)
coldest = min(temperature)
average = sum(temperature) / len(temperature)

above = 0
below = 0

for temp in temperature:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)
#30. Patient management using lists
patients = ["Aisha", "Rahul", "Sneha"]
ages = [20, 25, 22]

# Add patient
name = input("Enter new patient name: ")
age = int(input("Enter patient age: "))

patients.append(name)
ages.append(age)

# Delete patient
delete_name = input("Enter patient name to delete: ")

if delete_name in patients:
    index = patients.index(delete_name)
    patients.pop(index)
    ages.pop(index)
    print("Patient deleted.")
else:
    print("Patient not found.")

# Search patient
search_name = input("Enter patient name to search: ")

if search_name in patients:
    index = patients.index(search_name)
    print("Patient found.")
    print("Name:", patients[index])
    print("Age:", ages[index])
else:
    print("Patient not found.")

# Display all patients
print("\nAll Patients:")

for i in range(len(patients)):
    print("Name:", patients[i], "Age:", ages[i])

# Count patients
print("Total patients:", len(patients))
