# n = int(input("Enter number of students: "))

# marks = []

# for i in range(n):
#     mark = float(input(f"Enter marks of student {i + 1}: "))
#     marks.append(mark)

# maximum = max(marks)
# minimum = min(marks)
# average = sum(marks) / n

# above_average = 0
# for mark in marks:
#     if mark > average:
#         above_average += 1

# print("Maximum marks =", maximum)
# print("Minimum marks =", minimum)
# print("Average marks =", average)
# print("Students above average =", above_average)



# import numpy as np


# marks = np.array([
#     # Student 1
#     [[80, 85, 90], [70, 75, 80], [88, 90, 92]],

#     # Student 2
#     [[75, 80, 85], [65, 70, 75], [82, 85, 88]],

#     # Student 3
#     [[90, 92, 95], [80, 85, 90], [78, 82, 85]]
# ])


# subject_average = np.mean(marks, axis=(0, 2))

# print("Subject-wise average marks:")
# print(subject_average)


# n = int(input("Enter a number: "))

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print("Reversed number:", rev)  