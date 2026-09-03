#1.	Write a Python program to create a set containing five integers and display all its elements.
numbers = {10, 20, 30, 40, 50}
print("Set elements:")
for num in numbers:
    print(num)
    
    
#2.	Create a list containing duplicate values. Convert the list into a set and display the resulting set.
numbers = [10, 20, 10, 30, 20, 40, 30]
result = set(numbers)
print("Set after removing duplicates:", result)


#3.	Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
fruits.add("Pineapple")
fruits.add("Watermelon")
print("Updated set:", fruits)


#4.	Create a set of numbers and remove a specified number from the set.
numbers = {10, 20, 30, 40, 50}
num = int(input("Enter number to remove: "))
numbers.remove(num)
print("Updated set:", numbers)


#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Rahul", "Amit", "Sneha", "Priya", "Neha"}
name = input("Enter student name: ")
if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")
    
    
    
#6.	Create a set of cities and determine the total number of cities using an appropriate function.
cities = {"Pune", "Mumbai", "Kolhapur", "Delhi", "Nashik"}
print("Total number of cities:", len(cities))


#7.	Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C", "C++", "JavaScript"}
for language in languages:
    print(language)
    
    
#8.	Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [10, 20, 10, 30, 40, 20, 50, 30]
unique_numbers = set(numbers)
print("Numbers without duplicates:", unique_numbers)


#9.	Create two sets of integers and find their union.
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
result = set1.union(set2)
print("Union:", result)


#10.	Create two sets and find the elements common to both sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = set1.intersection(set2)
print("Common elements:", common)


'''11.	Create two sets and find:
•	Elements present in the first set but not the second 
•	Elements present in the second set but not the first'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
only_first = set1 - set2
only_second = set2 - set1
print("Present only in first set:", only_first)
print("Present only in second set:", only_second)


#12.	Create two sets of numbers and find the elements that are present in either set but not in both.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = set1.symmetric_difference(set2)
print("Elements in either set but not both:", result)


#13.	Create two sets and determine whether the first set is a subset of the second set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")
    
    
#14.	Create two sets and determine whether the first set is a superset of the second set.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
if set1.issuperset(set2):
    print("First set is a superset of second set.")
else:
    print("First set is not a superset of second set.")
    
    
#15.	Write a program to determine whether two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have common elements.")
    
    
#16.	Create two sets and check whether they are equal.
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}
if set1 == set2:
    print("Both sets are equal.")
else:
    print("Both sets are not equal.")
    
    
#17.	Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1 = {"Python", "Java", "DBMS", "Maths"}
student2 = {"Python", "C++", "DBMS", "OS"}
common = student1.intersection(student2)
print("Subjects studied by both students:", common)


#18.	Accept a sentence from the user and use a set to display all unique words.
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Unique words:")
for word in unique_words:
    print(word)
    
    
'''19.	Create two sets:
•	Students present in the morning session 
•	Students present in the afternoon session 
Find:
•	Students present in both sessions 
•	Students present only in the morning 
•	Students present only in the afternoon 
•	Students present in at least one session'''
morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Neha", "Kiran"}
both = morning.intersection(afternoon)
only_morning = morning - afternoon
only_afternoon = afternoon - morning
at_least_one = morning.union(afternoon)
print("Present in both sessions:", both)
print("Only in morning:", only_morning)
print("Only in afternoon:", only_afternoon)
print("Present in at least one session:", at_least_one)


'''20.	Create sets representing students enrolled in:
•	Python 
•	Java '''
python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Rahul", "Priya", "Neha", "Kiran"}
print("Python students:", python_students)
print("Java students:", java_students)


#21.	Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Rahul", "Priya", "Neha", "Kiran"}
both = python_students.intersection(java_students)
only_one = python_students.symmetric_difference(java_students)
print("Students enrolled in both:", both)
print("Students enrolled in only one course:", only_one)


'''22.	Create two sets representing technical skills of two employees. Find:
•	Common skills 
•	Skills unique to Employee 1 
•	Skills unique to Employee 2 
•	All available skills'''
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "JavaScript", "SQL", "Docker"}
common = employee1.intersection(employee2)
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1.union(employee2)
print("Common skills:", common)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)


#23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python", "Java", "C++", "DBMS", "Operating System"}
requested_books = {"Python", "DBMS", "HTML", "Java"}
available_requested = available_books.intersection(requested_books)
print("Requested books that are available:", available_requested)


'''24.	Store visitor IDs from two different days in separate sets. Determine:
•	Unique visitors across both days 
•	Returning visitors 
•	Visitors who came only on the first day 
•	Visitors who came only on the second day
•	Create sets representing products belonging to different categories. Find products that belong to both categories.'''
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}
unique_visitors = day1.union(day2)
returning_visitors = day1.intersection(day2)
only_first_day = day1 - day2
only_second_day = day2 - day1
print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", only_first_day)
print("Visitors only on second day:", only_second_day)


'''25.	Represent the friends of two users using sets. Find:
•	Mutual friends 
•	Friends unique to User 1 
•	Friends unique to User 2 
•	Total unique friends'''
user1 = {"Amit", "Rahul", "Sneha", "Priya"}
user2 = {"Rahul", "Priya", "Neha", "Kiran"}
mutual_friends = user1.intersection(user2)
unique_user1 = user1 - user2
unique_user2 = user2 - user1
total_friends = user1.union(user2)
print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_friends)