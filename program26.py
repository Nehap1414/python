# Create two tuples and find the common elements between them.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for item in tuple1:
    if item in tuple2:
        common = common + (item,)

print("Common elements:", common)