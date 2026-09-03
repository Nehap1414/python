# Create a tuple of colors. Check whether a given color exists in the tuple.
colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter a color: ")

if color in colors:
    print("Color exists in the tuple")
else:
    print("Color does not exist in the tuple")