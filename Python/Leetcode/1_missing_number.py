def missing_number(arr,n):
    #to calculate the sum of first n natural numbers
    sum_n = n * (n+1) / 2
    #to calculate sum of array
    sum_arr = sum(arr)
    
    missing_number = sum_n - sum_arr

    return missing_number

arr = [1,2,3,4,6]
n = 6
print(missing_number(arr,n))