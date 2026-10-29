
# Merge two tuples and remove duplicate elements.
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

result = ()

for item in merged:
    if item not in result:
        result = result + (item,)

print("Merged tuple without duplicates:", result)