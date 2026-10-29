# Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (50, 20, 40, 10, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Original tuple:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)