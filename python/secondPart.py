import numpy as np

# TODO (5) => Create a 3x3 array with integer random numbers between 5 and 20. Then, print the first column and the last row

array = np.random.randint(5, 21, (3,3))

print(array, end='\n\n') # full array
print(array[:, 0]) # first column
print(array[2, :], end='\n\n') # last row

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (6) => Create a random 3x3 array. Scroll each row with a loop and print the sum of each row

array = np.random.randint(5, 21, (3,3))
print(array, end='\n\n') # full array

for row in array:
    print(np.sum(row))
    
print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (7) => Generate an array with even numbers between 0 and 100 with List Comprehension

array = np.array([i for i in range(0, 101) if i % 2 == 0])
print(array)

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (8) => Create a 4x9 array. Resize it to 36 dimensions and 6x6

array = np.random.randint(10, 50, (4, 9))

print(array, end="\n\n") # original array
print(array.reshape(6, 6)) # 6x6 array

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (9) => Create a function that receives three arrays with the same format. Then, return them concatenated. If the arrays don't have with the same format, return an error message

def concatArray(firstArray, secondArray, thirdArray):
    if firstArray.shape != secondArray.shape or firstArray.shape != thirdArray.shape:
        raise Exception("The arrays don't have the same format.")
    
    return np.concatenate((firstArray, secondArray, thirdArray))

arrayOne = np.array([1,2,3])
arrayTwo = np.array([4,5,6])
arrayThree = np.array([7,8,9])

print(concatArray(arrayOne, arrayTwo, arrayThree))