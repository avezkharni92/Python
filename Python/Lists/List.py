#List is an Data Type
#Multiple types of data can be in list
#It is enclosed in Square bracket []
#Order will same unless changed


#Accessing the List 
shoppingList = ["Milk", "Cheese", "Butter"]

print(shoppingList[0])
print(shoppingList[-1])

#Traverse elemts of List 
for i in shoppingList:
    print(i)


for i in range(len(shoppingList)):
    print(shoppingList[i])

#Update/Insert List 

myList = [1,2,3,4,5,6,7]
print(myList)

#Order will same unless changed

myList[2] = 55
print(myList)

myList.insert(0,11)
print(myList)
myList.append(23)
print(myList)

myList.extend([11,12,13,14])
print(myList)


#Slice/delete in list 

myList1 = ['a', 'b', 'c', 'd', 'e', 'f']

print(myList1[::-1])
myList1[0:2] = ['x', 'y']
print(myList1)

#pop
myList1.pop(1)
print(myList1)

myList1.pop()
print(myList1)

del myList1[0:2]
print(myList1)

#remove funtion: remove the matching value. Believe 1st item
myList1.remove("e")
print(myList1)


#searching for an element in list

my_list2 = [10,20,30,40,50,60,70,80,90]

#using in operator
target = 50
if target in my_list2:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

#linear search

def linear_search(p_list, target):
    for i, value in enumerate(p_list):
        if value == target:
            return i
    return -1 

print(linear_search(my_list2, 40))

#List operations and List Functions
#concatenate list 


print(my_list2 + myList1)
print(len(my_list2))
print(max(my_list2))
print(min(my_list2))
print(sum(my_list2))

my_list2 = [10,20,30,40,50,60,70,80,90]
print(sum(my_list2)/len(my_list2))



#Calculating the average 
total = 0
count = 0

while True:
    inp = input("Enter a number")
    if inp == "Done" : break
    value = float(inp)
    total = total + value
    count = count+1
average = total/count
print(average)


#same above program using list

while True:
    inp = input("Enter a number")
    if inp == "Done" : break
    value = float(inp)
    total = total + value
    count = count+1
average = total/count
print(average)


new_list = list()
while True:
    inp = input("Enter a number")
    if inp == "Done" : break
    value = float(inp)
    new_list.append(value)
average = sum(new_list)/len(new_list)
print(average)
