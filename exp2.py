#Write a PYTHON program that reads a value of n and check the number is zero or non zero value.
from PIL.ImImagePlugin import number

n=int(input("enter the value of n:"))
if n==0:
    print("number is 0")
else:
    print("number is non zero")

#Write a PYTHON program to find a largest of two numbers.
num1=float(input("enter the 1st number:"))
num2=float(input("enter the 2nd number:"))
if num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")


#Write a PYTHON program that reads the number and check the no is positive or negative.
n=float(input("enter the number:"))
if n<0:
    print("number is negative")
else:
    print("number is positive")

#Write a PYTHON program to check entered character is vowel or consonant.
char=input("enter the character")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
    print("char is vowel")
else:
    print("char is consonant")


'''Write a PYTHON program to evaluate the student performance
      If % is >=90 then Excellent performance
      If % is >=80 then  Very Good performance
      If % is >=70 then Good performance
      If % is >=60 then average performance
      else Poor performance.'''

m=float(input("enter the marks:"))
if m>=90:
    print("excellent performance")
elif m>=80:
    print("very good performance")
elif m>=70:
    print("good performance")
elif m>=60:
    print("average performance")
else:
    print("poor performance")



#Write a PYTHON program to find largest of three numbers.
n1=int(input("enter the number 1:"))
n2=int(input("enter the number 2:"))
n3=int(input("enter the number 3:"))
if n1>n2 and n1>n3:
    print("number 1 is larger")
elif n2>n1 and n2>3:
    print("number 2 is larger")
else:
    print("number 3 is larger")


#Write a PYTHON program to find smallest of three numbers
n1=int(input("enter the number 1:"))
n2=int(input("enter the number 2:"))
n3=int(input("enter the number 3:"))
if n1<n2 and n1<n3:
    print("number 1 is smaller")
elif n2<n1 and n2<3:
    print("number 2 is smaller")
else:
    print("number 3 is smaller")

#Write a PYTHON program to check weather number is even or odd.
num=int(input("enter the number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

#Write a PYTHON program to check a year for leap year.
year=int(input("enter the year:"))
if year%4==0:
    print("it is leap year")
else:
    print("it is not a leap year")


'''A company insures its drivers in the following cases
1.if the driver is married
2.If the driver is unmarried, male and above 30 years        
         of age.
3.                 '''


married = input("Married? (yes/no): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if married == "yes":
    print("Driver is insured")
elif gender == "male" and age > 30:
    print("Driver is insured")
elif gender == "female" and age > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")

  '''while loop using
1.write a program to print the natual numbers up to n
2. to print even and odd numbers upto n
3.write a program to print sum of natual number upo n
4.write a program to print sum odd numbers
5.write a program to print sum odd numbers
6.write a program to print natual numbers upto n in reverse order
7.wp to print fibbonacci series upto n
8.write a program to cheack enter number is prime or not
9.wp find sum of digits of entered number
10.enter number is palindrome or not
11.wp to print multiplication table
12.wp to print largerst and smallest number from n numbers'''
