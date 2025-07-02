import array 

my_array = array.array("i")
print(my_array)
#Time Complexity = O(1)
#memory is in single row continously

my_array1 = array.array("i", [1, 2, 3, 4])
print(my_array1[2])
print(my_array1)
# Time complexity = O(n)

print("\n")

import numpy as np

my_array2 = np.array([], dtype = int)
print(my_array2)
#Time Complexity = O(1)

my_array3 = np.array([1,2,3,4, "a", 1.23])
print(my_array3)   
# Time complexity = O(n)


print("\n")

#Insertion of array
# Beginning , Middle/inbetween, End
my_array1.insert(0, 5)
print(my_array1)
#1st number is index where element need to be inserted and second is element
# Time complexity = O(n)


my_array1.insert(100, 50)
print(my_array1)

print("\n")

#Traverse of array 
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(my_array1)
#time complexity : O(n)
#Space complexity : O(1)

print("\n")

print('Search for an element in array')
#Linear Search

# Idea here is 
#1. Need for loop since each elemt is need to be checked 
#2. Put for loop inside a funtion since we can put array and target need to be compared with each element
#3. Take one element at a time and compare with element and find it's index and return
#4. If the element is not present then print -1
def linearSearch(array, target):
    for i in range(len(array)):
        if array[i]== target:
            return i
    return -1

print(linearSearch(my_array1, 50))
print(linearSearch(my_array1, 100))

print("\n")

print('Deleting an element from an array')
print(my_array1)
my_array1.remove(5)
my_array1.pop(2)
print(my_array1)








