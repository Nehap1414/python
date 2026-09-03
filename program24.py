# Store temperatures of seven days and determine maximum, minimum and average temperature.
temperatures = (32, 35, 31, 30, 34, 36, 33)

maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = sum(temperatures) / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)