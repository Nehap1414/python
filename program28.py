# Count the frequency of each element in a tuple.
numbers = (10, 20, 10, 30, 20, 10, 40)

checked = ()

for num in numbers:
    if num not in checked:
        print(num, "appears", numbers.count(num), "times")
        checked = checked + (num,)