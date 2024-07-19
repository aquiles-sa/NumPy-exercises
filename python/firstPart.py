import numpy as np

# TODO (1) => Create an array with numbers 0-9. Use only one dimension

array = np.arange(10)
print(array, end='\n\n')

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (2) => Create an array with numbers 0-9. Use List Comprehension

array = np.array([i for i in range(0, 10)])
print(array, end='\n\n')

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (3) => Create an array with numbers 0-8. Use two dimensions (3x3)

array = np.arange(9).reshape(3,3)
print(array, end='\n\n')

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (4) => Create a 2d array and print the first element of the first row and the last element of the last row
matrix = np.array([[1, 2], [3, 4]])

print(matrix[0][0]) # First element of the first row
print(matrix[1][0]) # First element of the first row
