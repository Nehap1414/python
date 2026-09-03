# Create a tuple with repeated numbers and count how many times a particular number appears.
numbers = (10, 20, 10, 30, 10, 40, 20)

num = int(input("Enter number: "))

print("Number of times", num, "appears:", numbers.count(num))