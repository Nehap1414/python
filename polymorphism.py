# 1. Shape Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):
    def area(self):
        return 5 * 4

class Triangle(Shape):
    def area(self):
        return 0.5 * 6 * 4

shapes = [Circle(), Rectangle(), Triangle()]
for s in shapes:
    print("Area:", s.area())


# 2. Employee Salary Polymorphism
class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 10000

class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 8000

class Tester(Employee):
    def calculate_salary(self):
        return 30000 + 5000

employees = [Manager(), Developer(), Tester()]
for e in employees:
    print("Salary:", e.calculate_salary())


# 3. Vehicle Start Polymorphism
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with key")

vehicles = [Car(), Bike(), Bus()]
for v in vehicles:
    v.start()


# 4. Animal Sound Polymorphism
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

class Cow(Animal):
    def sound(self):
        print("Cow says Moo")

class Lion(Animal):
    def sound(self):
        print("Lion says Roar")

animals = [Dog(), Cat(), Cow(), Lion()]
for a in animals:
    a.sound()


# 5. Notification Polymorphism
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")

notifications = [EmailNotification(), SMSNotification(), PushNotification()]
for n in notifications:
    n.send()


# 6. Student Grade Polymorphism
class Student:
    def calculate_grade(self):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self):
        print("Engineering grade: A")

class MedicalStudent(Student):
    def calculate_grade(self):
        print("Medical grade: A")

class ManagementStudent(Student):
    def calculate_grade(self):
        print("Management grade: A")

students = [EngineeringStudent(), MedicalStudent(), ManagementStudent()]
for s in students:
    s.calculate_grade()



# 7. Bank Account Interest Polymorphism
class BankAccount:
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 50000 * 0.06

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 50000 * 0.03

class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        return 50000 * 0.08

accounts = [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]
for a in accounts:
    print("Interest:", a.calculate_interest())



# 8. Report Polymorphism
class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF Report Generated")

class ExcelReport(Report):
    def generate(self):
        print("Excel Report Generated")

class HTMLReport(Report):
    def generate(self):
        print("HTML Report Generated")

def generate_report(report):
    report.generate()

generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())



# 9. Distance Operator Overloading
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches
        if inches >= 12:
            feet = feet + inches // 12
            inches = inches % 12
        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")

d1 = Distance(5, 8)
d2 = Distance(4, 7)
d3 = d1 + d2
d3.display()



# 10. Student Operator Overloading
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("A", 80)
s2 = Student("B", 70)
print("s1 > s2:", s1 > s2)
print("s1 < s2:", s1 < s2)



# 11. Product Operator Overloading
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 30000)
print("Same Price:", p1 == p2)
print("Laptop is Costlier:", p1 > p2)



# 12. Online Payment Polymorphism
class Payment:
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI payment of", amount, "successful")

class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card payment of", amount, "successful")

class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet payment of", amount, "successful")

def pay(payment, amount):
    payment.make_payment(amount)

pay(UPIPayment(), 1000)
pay(CardPayment(), 2000)
pay(WalletPayment(), 500)



# 13. Person Role Polymorphism
class Person:
    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print("I am a Student")

class Faculty(Person):
    def display_role(self):
        print("I am a Faculty")

class Administrator(Person):
    def display_role(self):
        print("I am an Administrator")

people = [Student(), Faculty(), Administrator()]
for p in people:
    p.display_role()



# 14. Media Polymorphism
class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print("Playing Audio")

class Video(Media):
    def play(self):
        print("Playing Video")

class Podcast(Media):
    def play(self):
        print("Playing Podcast")

media = [Audio(), Video(), Podcast()]
for m in media:
    m.play()



# 15. Smart Device Polymorphism
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print("Light ON")
    def turn_off(self):
        print("Light OFF")

class Fan(SmartDevice):
    def turn_on(self):
        print("Fan ON")
    def turn_off(self):
        print("Fan OFF")

class AC(SmartDevice):
    def turn_on(self):
        print("AC ON")
    def turn_off(self):
        print("AC OFF")

class TV(SmartDevice):
    def turn_on(self):
        print("TV ON")
    def turn_off(self):
        print("TV OFF")

devices = [Light(), Fan(), AC(), TV()]
for d in devices:
    d.turn_on()
    d.turn_off()


