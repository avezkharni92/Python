#For 2 dimentional array we use numpy

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np
twoDim = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9 ]])

print(twoDim)

#time_complexity = O(n) same space complexity as same memory will be acquired

#Adding column or row to the 2 dim array its time and space complexity of O(mn) using insert function

new_arr = np.insert(twoDim, 0, [1,2,3,4], axis = 1)
print(new_arr)

new_arr = np.insert(twoDim, 0, [1,2,3,4], axis = 0)
print(new_arr)
# appendindg array 1sst
# row or column where we want to insert
# what elements need to be inserted
# which axis row = 1 and colum = 0



# Accesing elements of array
print(new_arr[0][1])

#traverse through the TD array

def traverseTDarray(array):
    for i in range(len(array)):
       for j in range(len(array[0])):
           print(array[i][j])

traverseTDarray(new_arr)

#searching for an element in TD array
def traverseTDarray(array, target):
    for i in range(len(array)):
       for j in range(len(array[0])):
           if array[i][j] == target:
               print(f"The {target} is located in {i} row and {j} column position")
    return -1

traverseTDarray(new_arr, 5)


#Deleting the row or column 

new_arr = np.delete(twoDim, 0, axis = 0)
print(new_arr)