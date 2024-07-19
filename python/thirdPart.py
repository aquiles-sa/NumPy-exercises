import numpy as np

# TODO (10) => Create a function that split an array in n slices, but keep the absolute values.

def splitArray(array, slices):
    array = np.array_split(array, slices)
    return np.abs(array)

targetArray = np.array([1, 2, 3, -4, 5, -7])
number_slices = 2

print(splitArray(targetArray, number_slices))

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (11) => Create a function that receives an array and return the quantity of positive numbers.

def positiveNumbersQuantity(array):
    return len(np.where(array > 0)[0])
    

targetArray = np.array([1, 2, 3, 4, 5, -1, -3, -4, -9, 10, 11])
print(positiveNumbersQuantity(targetArray))

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (12) => Create a function that receives an array and return the index of the numbers that are divisible by 3.

def divisibleByThree(array):
    divisibles = np.where(array % 3 == 0)[0]
    return divisibles

targetArray = np.array([4, 5, 6, 7, 8, 9])
print(divisibleByThree(targetArray))

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (13) => Create a function that returns if an array contains negative numbers.

def checkNegatives(array):
    return np.any(array < 0)

targetArray = np.array([1, 2, 3, 4, -5])

print(checkNegatives(targetArray))


print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (14) => Create a function that receive an array and remove its negative numbers.

def removeNegativeNumbers(array):
    onlyPositives = array > 0
    return array[onlyPositives]

targetArray = np.array([1, 2, 3, 4, 5, -9, -8, -7, -6])
print(removeNegativeNumbers(targetArray))

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (15) => Create a function that receive an initial, final value and an array. The functions must return the numbers between the initial and final value inside a new array

def numbersBetweenValues(array, inital, final):
    numbers = (array >= inital) & (array <= final)
    return array[numbers]

targetArray = np.array([i for i in range(-10, 11)])

print(numbersBetweenValues(targetArray, inital=-7, final=7))

print("# --------------------------------------------------------------------#", end='\n\n')


# TODO (16) => Create a function that sorts an array and remove its odd numbers.

def sortArray(array):
    return np.sort(array)

def removeOddNumbers(array):
    onlyEven = array % 3 != 0
    return np.sort(array[onlyEven])
    
targetArray = np.array([10,3,5,7,9,2,5])
print(sortArray(targetArray))
print(removeOddNumbers(targetArray))

print("# --------------------------------------------------------------------#", end='\n\n')

# TODO (17) => Using the array of the last exercise, remove duplicated numbers.

def removeDuplicates(array):
    return np.unique(array)

print(removeDuplicates(targetArray))