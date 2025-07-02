# Methods in dictionary

myDict = {'name':'Edy', 'age':26, 'address':'london', 'education': 'master'}

print(myDict)



#clear() method would clear all the elements in dictiary and make it empty

myDict.clear()
#here notice that proniting along with clear method will give none output. to print empty dict use print seaprately
print(myDict)

myDict = {'name':'Edy', 'age':26, 'address':'london', 'education': 'master'}


#copy() method use the original and create new one withoud modifying the old one so we can use it for our use
myDict2 = myDict.copy()
print(myDict2)


#fromkeys method : used to assign same value to all the keys as shown below

newDict = {}.fromkeys([1,2,3], 0)

print(newDict)


#get() dictioanry , to get values from given dictionary.. syntax is .get(key, value(if its not in dict))

print(myDict.get('age', 27))
print(myDict.get('aged', 27))
#if there is no value given after the key above it will return none
print(myDict.get('aged'))

#to get the items in dictionary
print(myDict.items())

#To get the keys use .keys()
print(myDict.keys())

#ti return values
print(myDict.values())


#update method : it updates the dict by adding new values if key doesnt exist and if it is there it will update the dictionary
#to update we need to create new dictionary and then add it to the old dictionary
myDict1 = {'address':'btm', 'name':'avez'}

# so one thing to notice here that we cannot use print along with the update method.. print it separatelt
myDict.update(myDict1)
print(myDict)