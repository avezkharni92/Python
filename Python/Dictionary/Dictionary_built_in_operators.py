#Dictionary built-in operators

# In and no in operator 
# In operator will check for keys by default. if there then return True, if not then False
# not in will check for keys if there then false if not then true 
# in order to check values then use values() operator 

dict = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six"
}


print(1 in dict)
print(7 in dict)
print("One" in dict)
print("One" in dict.values())
print(1 not in dict)
print(0 not in dict)
print("One" not in dict.values())
print("Seven" not in dict.values())


# Len() function gives the number of keys in dictionary
print(len(dict))


#all function return true  if all values are present integers . if there is 0 or False then it will return false 

print(all(dict))

dict1 = {
    0 : "Zero",
    False : "False"
}

print(all(dict1))

# all() works like and function
# any() works like or function


#sorted list: keys are sorted
print(sorted(dict))