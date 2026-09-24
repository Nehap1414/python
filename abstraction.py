 #1. Shape Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
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



# 2. Vehicle Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")

vehicles = [Car(), Bike(), Bus()]
for v in vehicles:
    v.start()
    v.stop()



# 3. BankAccount Abstraction
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        print("Deposited", amount, "in Savings Account")

    def withdraw(self, amount):
        print("Withdrawn", amount, "from Savings Account")

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        print("Deposited", amount, "in Current Account")

    def withdraw(self, amount):
        print("Withdrawn", amount, "from Current Account")

accounts = [SavingsAccount(), CurrentAccount()]
for a in accounts:
    a.deposit(5000)
    a.withdraw(1000)



# 4. FoodOrder Abstraction
from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50

r = RestaurantOrder()
h = HomeDeliveryOrder()

print("Restaurant Total:", r.calculate_bill() + r.delivery_charge())
print("Home Delivery Total:", h.calculate_bill() + h.delivery_charge())



# 5. Patient Abstraction
from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment")

class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient treatment")

class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency treatment")

patients = [InPatient(), OutPatient(), EmergencyPatient()]
for p in patients:
    p.treatment()
    print("Bill:", p.calculate_bill())



# 6. Transport Abstraction
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 5

class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3

class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 12

class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15

transports = [Bus(), Train(), Taxi(), Flight()]

for t in transports:
    print("Fare:", t.calculate_fare(100))



# 7. Question Abstraction
from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self):
        pass

class MCQQuestion(Question):
    def evaluate_answer(self):
        print("MCQ answer checked")

class TrueFalseQuestion(Question):
    def evaluate_answer(self):
        print("True/False answer checked")

class DescriptiveQuestion(Question):
    def evaluate_answer(self):
        print("Descriptive answer checked")

questions = [MCQQuestion(), TrueFalseQuestion(), DescriptiveQuestion()]

for q in questions:
    q.evaluate_answer()



# 8. Authentication Abstraction
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Login using Password")

class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Login using OTP")

class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Login using Biometric")

methods = [PasswordAuthentication(), OTPAuthentication(), BiometricAuthentication()]

for m in methods:
    m.authenticate()



# 9. CloudStorage Abstraction
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")

class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")

storage = [GoogleDrive(), Dropbox()]

for s in storage:
    s.upload_file()
    s.download_file()
    s.delete_file()


# 10. Appointment Abstraction
from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500

class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000

class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 1500

appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for a in appointments:
    a.book_appointment()
    print("Fee:", a.calculate_fee())



