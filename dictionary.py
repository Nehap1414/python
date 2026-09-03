#1.	Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
student = {
    "roll_no": 101,
    "name": "Rahul",
    "department": "CSE",
    "marks": 85
}
for key, value in student.items():
    print(key, ":", value)
    
    
    
#2.	Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 55000
}
key = input("Enter key: ")
if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")
    
    
    
#3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 800,
    "Pencil": 5,
    "Bottle": 100
}
products["Notebook"] = 60
print(products)



#4.	Create a dictionary containing student marks. Update the marks of a specified student.
marks = {
    "Rahul": 80,
    "Amit": 75,
    "Sneha": 90
}
student = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))
if student in marks:
    marks[student] = new_marks
else:
    print("Student not found")
print(marks)



#5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities = {
    "Mumbai": 20,
    "Pune": 10,
    "Delhi": 19,
    "Kolhapur": 5
}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
else:
    print("City not found")
print(cities)



#6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha",
    104: "Priya"
}
emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")
    
    
    
#7.	Create a dictionary containing student records and find the total number of key-value pairs.
students = {
    "Rahul": 80,
    "Amit": 75,
    "Sneha": 90,
    "Priya": 85
}
print("Total key-value pairs:", len(students))



'''8.	Create a dictionary and display:
•	All keys 
•	All values 
•	All key-value pairs'''
student = {
    "Rahul": 80,
    "Amit": 75,
    "Sneha": 90
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Key-value pairs:", student.items())



#9.	Create a dictionary of programming languages and their creators. Display each key and value using a loop.
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}
for language, creator in languages.items():
    print(language, ":", creator)
    
    
    
#10.	Accept five student names and their marks from the user and store them in a dictionary.
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print(students)



#11.	Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
students = {
    "Rahul": 80,
    "Amit": 95,
    "Sneha": 88,
    "Priya": 91
}
highest_student = max(students, key=students.get)
print("Highest marks:", students[highest_student])
print("Student:", highest_student)



#12.	Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Rahul": 80,
    "Amit": 95,
    "Sneha": 68,
    "Priya": 91
}
lowest_student = min(students, key=students.get)
print("Lowest marks:", students[lowest_student])
print("Student:", lowest_student)



#13.	Create a dictionary containing student names and marks. Calculate the average marks of all students.
students = {
    "Rahul": 80,
    "Amit": 95,
    "Sneha": 88,
    "Priya": 91
}
average = sum(students.values()) / len(students)
print("Average marks:", average)



#14.	Accept a string from the user and create a dictionary containing each character and its frequency.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)



#15.	Accept a sentence and create a dictionary containing each word and the number of times it occurs.
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)



#16.	Create two dictionaries and merge them into a single dictionary.
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
merged = dict1.copy()
merged.update(dict2)
print(merged)


#17.	Given two dictionaries, find the keys that are common to both dictionaries.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}
common_keys = dict1.keys() & dict2.keys()
print("Common keys:", common_keys)



#18.	Given two dictionaries, identify the values that are common to both dictionaries.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 30, "z": 40}
common_values = set(dict1.values()) & set(dict2.values())
print("Common values:", common_values)



#19.	Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)



#20.	Create a dictionary and display its elements in ascending order of keys.
data = {
    "d": 40,
    "a": 10,
    "c": 30,
    "b": 20
}
sorted_data = dict(sorted(data.items()))
print(sorted_data)



#21.	Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print(squares)



#22.	Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2
print(squares)


#23.	Given a list of numbers, create a dictionary containing each unique number and its frequency.
squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2
print(squares)



#24.	Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)



'''25.	Create a dictionary containing student names and marks. Develop a program to:
•	Add a student 
•	Update marks 
•	Delete a student 
•	Search for a student 
•	Display all students 
•	Find the highest marks 
•	Calculate the average'''
students = {
    "Rahul": 80,
    "Amit": 90,
    "Sneha": 85
}
while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")
    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")
    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")
    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)
    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print("Highest:", name, students[name])
    elif choice == 7:
        if students:
            print("Average:", sum(students.values()) / len(students))
    elif choice == 8:
        break
    else:
        print("Invalid choice")
        
        
        
'''26.	Create a dictionary containing employee names and salaries. Find:
•	Highest salary 
•	Lowest salary 
•	Average salary 
•	Employees earning more than ₹50,000'''
employees = {
    "Rahul": 45000,
    "Amit": 60000,
    "Sneha": 75000,
    "Priya": 50000
}
highest = max(employees, key=employees.get)
lowest = min(employees, key=employees.get)
average = sum(employees.values()) / len(employees)
print("Highest salary:", highest, employees[highest])
print("Lowest salary:", lowest, employees[lowest])
print("Average salary:", average)
print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)
        
        
        
        
'''27.	Create a dictionary containing product names and quantities.
Perform:
•	Add a product 
•	Update quantity 
•	Delete a product 
•	Search for a product 
•	Display products with quantity below 10'''
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}
while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Quantity Below 10")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity
    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
        else:
            print("Product not found")
    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")
    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print("Quantity:", products[name])
        else:
            print("Product not found")
    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, quantity)
    elif choice == 6:
        break
    else:
        print("Invalid choice")
        
        
        
        
'''28.	Create a dictionary containing names and phone numbers.
Implement:
•	Add contact 
•	Search contact 
•	Update contact 
•	Delete contact 
•	Display all contacts'''
contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}
while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")
    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")
    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found")
    elif choice == 5:
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == 6:
        break
    else:
        print("Invalid choice")
        
        
        
'''29.	Create a dictionary containing book IDs and book names.
Implement:
•	Add a book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books'''
books = {
    101: "Python",
    102: "Java",
    103: "C Programming"
}
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display Books")
    print("5. Count Books")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print("Book:", books[book_id])
        else:
            print("Book not found")
    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
        else:
            print("Book not found")
    elif choice == 4:
        for book_id, name in books.items():
            print(book_id, ":", name)
    elif choice == 5:
        print("Total books:", len(books))
    elif choice == 6:
        break
    else:
        print("Invalid choice")
        
        
        
#30.	Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
students = {
    "Rahul": "CSE",
    "Amit": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Riya": "IT"
}
groups = {}
for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)
print(groups)



#31.	Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.
words = ["cat", "dog", "apple", "banana", "sun", "book"]
result = {}
for word in words:
    length = len(word)
    if length not in result:
        result[length] = []
    result[length].append(word)
print(result)



#32.	Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
words = ["cat", "dog", "apple", "banana", "sun", "book"]
result = {}
for word in words:
    length = len(word)
    if length not in result:
        result[length] = []
    result[length].append(word)
print(result)



#33.	Take a string, use a dictionary to find the first character that occurs only once.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break
    
    
    
#34.	Take a string, use a dictionary to find the first character that occurs more than once.
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break
    
    
    
'''35.	Accept a paragraph and create a dictionary where:
•	Key = word length 
•	Value = number of words having that length.'''
paragraph = input("Enter a paragraph: ")
words = paragraph.split()
result = {}
for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1
print("Word length : Number of words")
for length, count in result.items():
    print(length, ":", count)

