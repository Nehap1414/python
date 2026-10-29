a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Largest Number =", largest)
print("Smallest Number =", smallest)