#we can define dictionary using 2 ways. 1. using dict()   2. {}

#creating an empty dictionary 
dict1 = dict()
dict2 = {}
print(dict1)
print(dict2)


#3 ways to define non-empty dictionary 
#example english to spanish

#1. using dict()
dict3 = dict(one='ones', two = 'dros', three= 'tres')
print(dict3)

#2 using {}
dict4 = {'one':"ones", "two":"dros", "three":"tres"}
print(dict4)

#using tuple/list to dictionary conversion
dict5 = [('one','ones'), ('two', 'dros'), ('three','tres')]

dict6 = dict(dict5)
print(dict6)

#Time and space complexity is O(n)


#Update the element of an array
dict7 = {'name':'Edy', 'age': 26}
dict7['age'] = 27
print(dict7)

dict7['address'] = 'Earth'
print(dict7)


#Traverse through the dictionary = means listing all elements of array

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
        print(key)
        print(dict[key])

traverseDict(dict7)


#Searching for an element in a dictionary. Linear search means traversing through the dictionary


def searchValue(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Value doesn't exist in dictionary"

print(searchValue(dict7, 25))
print(searchValue(dict7, 27))


# Delete or remove an element from an dictionary
#using delete

del dict7['name']
print(dict7)

#using pop method

dict8 = dict7.pop('age', None)
#To remove last element from dictionary
dict9 = dict7.popitem()

print(dict8)
print(dict9)
print(dict7)
