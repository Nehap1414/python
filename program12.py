# Accept five numbers from the user, store them in a list, and convert the list into a tuple.
numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

my_tuple = tuple(numbers)

print("List:", numbers)
print("Tuple:", my_tuple)