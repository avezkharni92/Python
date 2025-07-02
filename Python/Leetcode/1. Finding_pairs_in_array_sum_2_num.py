# Here we need to find all the pairs whose sum is equal to target
# One condition is both the elements should not be equal
# Get the array and target 
# Have 2 for loops
# 1st loop to start from 0  and goes till last but 1 and 2nd to start from 1st element 
# check for condition if both the elements are equal if so then continue to next element
# check if both sum is eaul to target
# return the idex values


def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range((i+1), len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i, j)
        
arr = [1, 2, 3, 4, 5, 6]
target = 5
two_sum(arr, target)
        
