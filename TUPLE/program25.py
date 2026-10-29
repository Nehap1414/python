# Store runs scored in 10 matches and calculate total, highest, lowest and average score.
runs = (45, 67, 23, 89, 56, 78, 34, 90, 55, 72)

total = sum(runs)
average = total / len(runs)

highest = runs[0]
lowest = runs[0]

for score in runs:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)