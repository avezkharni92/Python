print("1. Create an array and traverse.\n")

import array
#For array 1st data type need to be given then the elemeents in an bracket
my_array = array.array("i", [1,2,3,4,5])
print(my_array)
def traverseArray(array):
    for i in array:
        print(i)
traverseArray(my_array)

print("\n2. Access individual elements through indexes\n")

def individual_array(array, index):
    print(array[index])
individual_array(my_array, 2)



print("\n3. Append any value to the array using append() method")
#append insert the element at end of array
my_array.append(6)
print(my_array)

print("\n4. Insert value in an array using insert() method")

my_array.insert(0, 9)
#Here 1st is index wherever we want to place our value of element and then 2nd is the element 
print(my_array)


print("\n5. Extend python array using extend() method")
#Here we can extend more than one value at the end of array. extension of append function. 
my_array.extend([10, 11, 12, 13])
print(my_array)

print("\n6. Add items from list into array using fromlist() method")
#Array is not built-in in python, instead we have list 
tempist = [13, 14, 15, 16]
my_array.fromlist(tempist)
print(my_array)

print("\n7. Remove any array element using remove() method")
#Remove funrtion removes the matched element, not the index, 
#If there are more than one match to the element then the first matched will be deleted

my_array.remove(13)
print(my_array)

print("\n8. Remove last array element using pop() method")
# Pop removes the element in given index
my_array.pop(4)
print(my_array)

print("\n9. Fetch any element through its index using index() method")

index_1 = my_array.index(2)
print(index_1)

print("\n10. Reverse a python array using reverse() method")

print(my_array.reverse())
print(my_array)

print("\n11. Get array buffer information through buffer_info() method")
print(my_array.buffer_info())

print("\n12. Check for number of occurrences of an element using count () method")
my_array.append(5)
count1 = my_array.count(5)
print(count1)

print("\n13. Convert array to string using tostring() method")
#tostring converts a daratype into string
#fromstring converts the strint to other data type
#from array import *
#str_temp = my_array.tostring()
#print(str_temp)


print("\n14. Convert array to a python list with same elements using tolist() method")
print("\n15. Append a string to char array using fromstring() method")
print("\n16. Slice Elements from an array")

print(my_array[1:4])
print(my_array)
print(my_array[::-1])
print(my_array[-5:])
