import numpy as np

print("=" * 60)
print("NUMPY PRACTICAL PROGRAMS")
print("=" * 60)


print("\n1. One-Dimensional Array")

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)


print("\n2. Arithmetic Operations")

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Array A:", a)
print("Array B:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)



print("\n3. Array Statistics")

arr = np.array([10, 25, 30, 45, 50, 65, 70, 80, 90, 100])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))



print("\n4. Even and Odd Numbers")

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)



print("\n5. Reshaping Array")

arr = np.arange(1, 13)

print("Original Array:", arr)
print("2 x 6 Matrix:\n", arr.reshape(2, 6))
print("3 x 4 Matrix:\n", arr.reshape(3, 4))
print("4 x 3 Matrix:\n", arr.reshape(4, 3))



print("\n6. Matrix Addition")

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Addition:\n", matrix1 + matrix2)



print("\n7. Matrix Multiplication")

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix Multiplication:\n", np.matmul(matrix1, matrix2))



print("\n8. Matrix Transpose")

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original Matrix:\n", matrix)
print("Transpose:\n", matrix.T)



print("\n9. Accessing Matrix Elements")

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:\n", matrix)
print("First Row:", matrix[0])
print("Last Column:", matrix[:, -1])
print("Diagonal Elements:", np.diag(matrix))
print("Second and Third Rows:\n", matrix[1:3])


print("\n10. Row and Column Sum")

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:\n", matrix)
print("Sum of Each Row:", np.sum(matrix, axis=1))
print("Sum of Each Column:", np.sum(matrix, axis=0))



print("\n11. Array Slicing")

arr = np.arange(1, 21)

print("Array:", arr)
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])



print("\n12. Boolean Indexing Replacement")

arr = np.array([10, 25, 55, 70, 45, 80, 30, 90, 15, 60])

print("Original Array:", arr)

arr[arr > 50] = 0

print("After Replacement:", arr)



print("\n13. Sorting Array")

arr = np.array([50, 10, 80, 30, 90, 20, 70, 40])

print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])



print("\n14. Unique Elements")

arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40, 50])

print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))



print("\n15. Concatenation")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Array A:\n", a)
print("Array B:\n", b)

print("Horizontal Concatenation:\n", np.hstack((a, b)))
print("Vertical Concatenation:\n", np.vstack((a, b)))



print("\n16. Student Marks Statistics")

marks = np.array([78, 85, 90, 65, 72, 88, 95, 60, 82, 75])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))



print("\n17. Marks Above Class Average")

marks = np.array([
    55, 60, 72, 80, 45,
    90, 65, 78, 88, 50,
    92, 70, 68, 85, 76,
    95, 58, 62, 82, 74
])

average = np.mean(marks)

print("Marks:", marks)
print("Class Average:", average)
print("Students Scoring Above Average:", marks[marks > average])



print("\n18. 3D Array")

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


print("\n19. Accessing 3D Array Elements")

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr)
print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


print("\n20. Sum of 3D Array")

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr)
print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=2))
print("Sum Along Columns:", np.sum(arr, axis=1))


print("\n21. Replace Values Greater Than 50")

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:\n", arr)

arr[arr > 50] = 0

print("After Replacement:\n", arr)



print("\n22. Random 3D Array Statistics")

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:\n", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23. Flatten 3D array
print("\n23. Flatten 3D Array")

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array:\n", arr)

flat = arr.flatten()

print("Flattened Array:", flat)


# 24. Flatten array and calculate statistics
print("\n24. Flatten and Calculate Statistics")

arr = np.arange(1, 28).reshape(3, 3, 3)

flat = arr.flatten()

print("Original 3D Array:\n", arr)
print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# 25. Random 3D array and filtering
print("\n25. Random 3D Array Filtering")

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array:\n", arr)

flat = arr.flatten()
average = np.mean(flat)

print("Elements Greater Than 50:", flat[flat > 50])
print("Even Numbers:", flat[flat % 2 == 0])
print("Average:", average)
print("Elements Less Than Average:", flat[flat < average])


print("\n" + "=" * 60)
print("ALL 25 NUMPY PROGRAMS COMPLETED")
print("=" * 60)