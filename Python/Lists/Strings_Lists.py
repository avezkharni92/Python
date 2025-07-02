#To convert list into string

a = 'Spam'
b = list(a)
print(b)

#we can split a string into list using split function
a = "spam spam spam"
b = a.split()
print(b)

#if there is special character in string then we can use it as delimiter and split the string
a = "spam1-spam2-spam3"
delimiter = "-"
b = a.split(delimiter)
print(b)
print(delimiter.join(b))
delimiter = " "
print(delimiter.join(b))


#sort is used to sort in incremental order
my_list4 = [5,2,3,1,6,7,4,7,5]
print(my_list4)
#One thing to notice here dont put print for sort .. use it separately
my_list4.sort()
print(my_list4)