# 1. Employee and Manager - Single Inheritance
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)

m = Manager(101, "Ashwini", 30000, "IT")
m.display()


# 2. Vehicle and Car - Single Inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.price * 0.90)

c = Car("Tata", "Nexon", "Petrol", 900000)
c.display()



# 3. Academic and Sports - Multiple Inheritance
class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, points):
        self.points = points

class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        print("Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", self.marks + self.points)

s = Student(80, 15)
s.performance()



# 4. PersonalDetails and ProfessionalDetails - Multiple Inheritance
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

e = Employee("Rahul", 25, 102, "Developer", 40000)
e.display()



# 5. Person -> Student -> ResearchStudent - Multilevel Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name, self.age, self.roll_no, self.course)
        print(self.topic, self.guide)

r = ResearchStudent("Priya", 22, 12, "CSE", "AI", "Dr. Patil")
r.display()



# 6. BankAccount -> SavingsAccount -> PremiumSavingsAccount - Multilevel
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, rate):
        super().__init__(acc_no, balance)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate / 100

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_no, balance, rate, benefits):
        super().__init__(acc_no, balance, rate)
        self.benefits = benefits

    def display(self):
        print("Account:", self.acc_no)
        print("Balance:", self.balance)
        print("Interest:", self.interest())
        print("Benefits:", self.benefits)

p = PremiumSavingsAccount(1001, 50000, 6, "Free ATM")
p.display()



# 7. Shape -> Circle, Rectangle, Triangle - Hierarchical Inheritance
class Shape:
    def name(self):
        print("This is a shape")

class Circle(Shape):
    def area(self, r):
        print("Circle Area:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self, l, b):
        print("Rectangle Area:", l * b)

class Triangle(Shape):
    def area(self, b, h):
        print("Triangle Area:", 0.5 * b * h)

Circle().area(5)
Rectangle().area(5, 4)
Triangle().area(6, 4)


# 8. Employee -> Manager, Developer, Tester - Hierarchical Inheritance
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Manager(Employee):
    def total_salary(self):
        return self.salary + 10000

class Developer(Employee):
    def total_salary(self):
        return self.salary + 8000

class Tester(Employee):
    def total_salary(self):
        return self.salary + 5000

print("Manager Salary:", Manager(1, "A", 30000).total_salary())
print("Developer Salary:", Developer(2, "B", 30000).total_salary())
print("Tester Salary:", Tester(3, "C", 30000).total_salary())



# 9. Person -> Student, Faculty -> TeachingAssistant - Hybrid Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class Faculty(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll_no, subject):
        Person.__init__(self, name)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)

ta = TeachingAssistant("Neha", 20, "Python")
ta.display()



# 10. Vehicle -> Car/Bike -> SportsCar/ElectricBike - Hybrid/Hierarchical
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def car_info(self):
        print("Car:", self.brand)

class Bike(Vehicle):
    def bike_info(self):
        print("Bike:", self.brand)

class SportsCar(Car):
    def speed(self):
        print("Sports Car speed is high")

class ElectricBike(Bike):
    def battery(self):
        print("Electric Bike has battery")

SportsCar("BMW").speed()
ElectricBike("Ola").battery()



# 11. Student -> Result - Single Inheritance
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def result(self, m1, m2, m3):
        total = m1 + m2 + m3
        percentage = total / 3
        print("Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)
        if percentage >= 75:
            print("Grade: A")
        elif percentage >= 60:
            print("Grade: B")
        else:
            print("Grade: C")

Result(1, "A", "CSE").result(80, 70, 90)



# 12. Product -> ElectronicProduct - Single Inheritance
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self):
        print("Final Price:", self.price * 0.90)

ElectronicProduct(1, "Laptop", 60000, "HP", "2 Years").final_price()



# 13. Printer and Scanner -> MultifunctionDevice - Multiple Inheritance
class Printer:
    def print_document(self):
        print("Printing document")

class Scanner:
    def scan_document(self):
        print("Scanning document")

class MultifunctionDevice(Printer, Scanner):
    pass

d = MultifunctionDevice()
d.print_document()
d.scan_document()



# 14. Camera and Phone -> Smartphone - Multiple Inheritance
class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()
s.take_photo()
s.make_call()


# 15. Person -> Student -> ResearchStudent - Multilevel Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll, course, topic, guide):
        super().__init__(name, age, roll, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name, self.age, self.roll, self.course, self.topic, self.guide)

ResearchStudent("Riya", 23, 15, "CSE", "ML", "Dr. Rao").display()



# 16. Person -> Student -> ResearchStudent - Multilevel Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll, course, topic, guide):
        super().__init__(name, age, roll, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll:", self.roll)
        print("Course:", self.course)
        print("Topic:", self.topic)
        print("Guide:", self.guide)

ResearchStudent("Amit", 24, 16, "CSE", "Data Science", "Dr. Joshi").display()



# 17. Animal -> Dog, Cat, Cow - Hierarchical Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")

class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow")

class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo")

Dog("Dog").sound()
Cat("Cat").sound()
Cow("Cow").sound()




# 18. Person -> Doctor, Patient with Surgeon/MedicalResearcher - Hybrid
class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def doctor_info(self):
        print(self.name, "is a Doctor")

class Patient(Person):
    def patient_info(self):
        print(self.name, "is a Patient")

class Surgeon(Doctor, Patient):
    def surgery(self):
        print(self.name, "performs surgery")

class MedicalResearcher(Doctor):
    def research(self):
        print(self.name, "does medical research")

Surgeon("Dr. Amit").surgery()
MedicalResearcher("Dr. Neha").research()



