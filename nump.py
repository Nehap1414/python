
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.matmul(A, B)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix multiplication (A × B):")
print(C)



numbers = [64, 34, 25, 12, 22, 11, 90]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)



filename = input("Enter the file name: sample.txt ")
word = input("Enter the word to search:  ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.lower().split()
    frequency = words.count(word.lower())

    print("Frequency of", word, ":", frequency)

except FileNotFoundError:
    print("Error: File not found.")






