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

#1.write a program to print the natual numbers up to n
n=int(input("enter the number"))
i=1
while i<=n:
    print("natual number are")
    i+=1

#2. to print even and odd numbers upto n
num=int(input("enter the number"))
i=1
print("even number")
while i<=num:
    if i%2==0:
        print(i)
    i=i+1
i=1
print("odd number")
while i<=num:
    if i%2!=0:
        print(i)
    i=i+1

#4.write a program to print sum even numbers
n=int(input("Enter the value of n: "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("Sum of even numbers =", sum)

#5.write a program to print sum odd numbers
n=int(input("Enter the value of n: "))
i=1
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i=i+1
print("Sum of odd numbers =", sum)


#write a program to print sum of natual number upo n
n=int(input("Enter the value of n: "))
i=1
sum=0
while i<=n:
    sum =sum+i
    i=i+1
print("Sum of natural numbers =", sum)

#write a program to print natual numbers upto n in reverse order
n=int(input("Enter the value of n: "))
while n>=1:
    print(n)
    n=n-1


#wp to print fibbonacci series upto n
n=int(input("Enter the number of terms: "))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1

#8.write a program to cheack enter number is prime or notn = int(input("Enter a number: "))

i=2
while i<n:
    if n%i==0:
        print("Not a Prime Number")
        break
    i=i+1
else:
    print("Prime Number")

#9.wp find sum of digits of entered number
n=int(input("Enter a number: "))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10

print("Sum of digits =", sum)

#10.enter number is palindrome or not
n=int(input("Enter a number: "))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


#11.wp to print multiplication table
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1


#12.wp to print largerst and smallest number from n numbers
n=int(input("Enter how many numbers: "))
num=int(input("Enter number: "))
largest=num
smallest=num
i=1
while i<n:
    num=int(input("Enter number: "))
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
    i=i+1
print("Largest number =",largest)
print("Smallest number =",smallest)