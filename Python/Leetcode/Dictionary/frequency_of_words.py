#Define a function to count the frequency of words in a given list of words.

#Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
##count_word_frequency(words) 
#Output:

# {'apple': 3, 'orange': 2, 'banana': 1}

#my solution 
#1. create an empty dictionary
# 2. Traverse through the value of each element 
#3. if that value is present in dictionary then update if not add it

def count_word_frequency(words):
    new_dict = {}
    for i in words:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] +=1
    return new_dict

print(count_word_frequency(words))
