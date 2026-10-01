import pandas as pd

print("=" * 70)
print("PANDAS PRACTICAL PROGRAMS")
print("=" * 70)



print("\n\n1. STUDENT DATAFRAME")

student_data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Neha"],
    "Python": [85, 70, 92, 78, 88],
    "DBMS": [80, 75, 90, 82, 85],
    "Mathematics": [90, 72, 95, 80, 87]
}

df = pd.DataFrame(student_data)

print("\nStudent DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df)

print("\nStudents with Average Marks greater than 75:")
print(df[df["Average"] > 75])



print("\n\n2. EMPLOYEE DATAFRAME")

employee_data = {
    "Employee_ID": [201, 202, 203, 204, 205],
    "Employee_Name": ["Amit", "Riya", "Karan", "Sneha", "Rahul"],
    "Department": ["CSE", "HR", "IT", "CSE", "Finance"],
    "Salary": [45000, 60000, 75000, 52000, 90000],
    "Experience": [2, 5, 7, 4, 10]
}

df = pd.DataFrame(employee_data)

print("\nEmployee DataFrame:")
print(df)

print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with Highest Experience:")
print(df.loc[df["Experience"].idxmax()])


print("\n\n3. PRODUCT DATAFRAME")

product_data = {
    "Product_ID": [301, 302, 303, 304, 305],
    "Product_Name": ["Laptop", "Mobile", "Tablet", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Price": [50000, 25000, 30000, 2000, 15000],
    "Quantity": [2, 5, 3, 10, 4]
}

df = pd.DataFrame(product_data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("\nProduct DataFrame:")
print(df)

print("\nProduct with Highest Total Sales:")
print(df.loc[df["Total_Amount"].idxmax()])



print("\n\n4. PATIENT DATAFRAME")

patient_data = {
    "Patient_ID": [401, 402, 403, 404, 405],
    "Patient_Name": ["Raj", "Meena", "Suresh", "Anita", "Vijay"],
    "Age": [45, 65, 72, 55, 68],
    "Disease": ["Diabetes", "Heart Disease", "Cancer", "Fever", "Diabetes"],
    "Medical_Charges": [30000, 75000, 120000, 25000, 60000]
}

df = pd.DataFrame(patient_data)

print("\nPatient DataFrame:")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())

print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])



print("\n\n5. ORDER DATAFRAME")

order_data = {
    "Order_ID": [501, 502, 503, 504, 505],
    "Customer": ["Amit", "Riya", "Karan", "Neha", "Priya"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [2, 3, 2, 4, 1],
    "Price": [50000, 25000, 30000, 15000, 12000],
    "Discount": [5000, 2000, 3000, 1000, 500]
}

df = pd.DataFrame(order_data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("\nAll Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest Value Order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())



print("\n\n6. STUDENT ATTENDANCE")

attendance_data = {
    "Student_ID": [601, 602, 603, 604, 605],
    "Name": ["Amit", "Riya", "Neha", "Karan", "Priya"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 120, 90, 110],
    "Classes_Attended": [85, 70, 80, 65, 100]
}

df = pd.DataFrame(attendance_data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("\nAttendance DataFrame:")
print(df)

print("\nStudents with Attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])



print("\n\n7. RETAIL SHOP SALES")

retail_data = {
    "Product_ID": [701, 702, 703, 704, 705],
    "Product_Name": ["Laptop", "Mobile", "TV", "Keyboard", "Headphones"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Price": [55000, 20000, 40000, 1500, 3000],
    "Quantity": [2, 5, 3, 10, 8]
}

df = pd.DataFrame(retail_data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\nRetail DataFrame:")
print(df)

print("\nProducts with Sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())



print("\n\n8. STUDENT MARKS SERIES")

student_marks = pd.Series({
    "Amit": 85,
    "Riya": 72,
    "Neha": 92,
    "Karan": 68,
    "Priya": 80
})

print("\nStudent Marks Series:")
print(student_marks)

print("\nMarks of Neha:")
print(student_marks["Neha"])

print("\nMaximum Marks:")
print(student_marks.max())

print("\nMinimum Marks:")
print(student_marks.min())

print("\nAverage Marks:")
print(student_marks.mean())

print("\nStudents scoring more than 75:")
print(student_marks[student_marks > 75])



print("\n\n9. EMPLOYEE SALARY SERIES")

employee_salary = pd.Series({
    "Amit": 45000,
    "Riya": 60000,
    "Karan": 75000,
    "Sneha": 48000,
    "Rahul": 90000
})

print("\nEmployee Salary Series:")
print(employee_salary)

print("\nHighest Salary:")
print(employee_salary.max())

print("\nLowest Salary:")
print(employee_salary.min())

print("\nAverage Salary:")
print(employee_salary.mean())

print("\nEmployees earning more than 50000:")
print(employee_salary[employee_salary > 50000])



print("\n\n10. PRODUCT PRICE SERIES")

product_prices = pd.Series({
    "Laptop": 50000,
    "Mobile": 25000,
    "Tablet": 30000,
    "Keyboard": 1500,
    "Mouse": 800
})

print("\nProduct Prices:")
print(product_prices)

product_prices = product_prices * 1.10

print("\nPrices after 10% increase:")
print(product_prices)

print("\nMost Expensive Product:")
print(product_prices.idxmax(), "=", product_prices.max())

print("\nProducts costing more than 1000:")
print(product_prices[product_prices > 1000])


print("\n\n11. PATIENT AGE SERIES")

patient_ages = pd.Series({
    "P001": 45,
    "P002": 65,
    "P003": 72,
    "P004": 50,
    "P005": 68
})

print("\nPatient Ages:")
print(patient_ages)

print("\nAverage Age:")
print(patient_ages.mean())

print("\nOldest Patient:")
print(patient_ages.idxmax(), "=", patient_ages.max())

print("\nYoungest Patient:")
print(patient_ages.idxmin(), "=", patient_ages.min())

print("\nPatients above 60:")
print(patient_ages[patient_ages > 60])



print("\n\n12. STUDENT ATTENDANCE SERIES")

student_attendance = pd.Series({
    "Amit": 85,
    "Riya": 72,
    "Neha": 95,
    "Karan": 68,
    "Priya": 92
})

print("\nStudent Attendance:")
print(student_attendance)

print("\nAverage Attendance:")
print(student_attendance.mean())

print("\nAttendance below 75%:")
print(student_attendance[student_attendance < 75])

print("\nAttendance above 90%:")
print(student_attendance[student_attendance > 90])

print("\nHighest Attendance:")
print(student_attendance.max())



print("\n\n13. STUDENTS CSV FILE")

try:
    df = pd.read_csv("students.csv")

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nLast 5 Records:")
    print(df.tail())

    df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
    df["Average"] = df["Total"] / 3

    print("\nTotal and Average Marks:")
    print(df)

    print("\nStudents with Average greater than 75:")
    print(df[df["Average"] > 75])

    print("\nStudent with Highest Average:")
    print(df.loc[df["Average"].idxmax()])

    print("\nAverage Marks of Each Subject:")
    print(df[["Python", "DBMS", "Maths"]].mean())

except FileNotFoundError:
    print("students.csv file not found.")



print("\n\n14. EMPLOYEES CSV FILE")

try:
    df = pd.read_csv("employees.csv")

    print("\nEmployees from CSE Department:")
    print(df[df["Department"] == "CSE"])

    print("\nAverage Salary:")
    print(df["Salary"].mean())

    print("\nHighest Salary:")
    print(df["Salary"].max())

    print("\nLowest Salary:")
    print(df["Salary"].min())

    print("\nEmployees with Salary greater than 50000:")
    print(df[df["Salary"] > 50000])

    print("\nDepartment-wise Average Salary:")
    print(df.groupby("Department")["Salary"].mean())

except FileNotFoundError:
    print("employees.csv file not found.")



print("\n\n15. PATIENTS CSV FILE")

try:
    df = pd.read_csv("patients.csv")

    print("\nPatients above 60 years:")
    print(df[df["Age"] > 60])

    print("\nAverage Medical Expense:")
    print(df["Medical_Expense"].mean())

    print("\nPatient with Highest Medical Expense:")
    print(df.loc[df["Medical_Expense"].idxmax()])

    print("\nNumber of Patients for Each Disease:")
    print(df["Disease"].value_counts())

    print("\nPatients with Medical Expense greater than 50000:")
    print(df[df["Medical_Expense"] > 50000])

except FileNotFoundError:
    print("patients.csv file not found.")



print("\n\n16. WEATHER CSV FILE")

try:
    df = pd.read_csv("weather.csv")

    print("\nMaximum Temperature:")
    print(df["Temperature"].max())

    print("\nMinimum Temperature:")
    print(df["Temperature"].min())

    print("\nAverage Temperature:")
    print(df["Temperature"].mean())

    print("\nRecords where Temperature is above 35°C:")
    print(df[df["Temperature"] > 35])

    print("\nCity-wise Average Temperature:")
    print(df.groupby("City")["Temperature"].mean())

except FileNotFoundError:
    print("weather.csv file not found.")


print("\n" + "=" * 70)
print("ALL PANDAS PROGRAMS COMPLETED")
print("=" * 70)