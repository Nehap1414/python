per = float(input("Enter Percentage: "))

if per > 90:
    print("Excellent")
elif per > 80:
    print("Very Good")
elif per > 70:
    print("Good")
elif per > 60:
    print("Average")
else:
    print("Worst Performance")