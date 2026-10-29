# Find the largest and smallest number in a tuple without using max() and min().
numbers = (45, 12, 78, 34, 90, 23)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)