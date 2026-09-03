# Modify a tuple by converting it into a list and then back into a tuple.
numbers = (10, 20, 30, 40)

my_list = list(numbers)

my_list[1] = 25

numbers = tuple(my_list)

print("Modified tuple:", numbers)