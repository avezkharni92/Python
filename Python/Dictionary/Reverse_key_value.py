def reverse_dict(my_dict):
    reversed_dict = {}  # Create a new dictionary to store reversed key-value pairs
    for key, value in my_dict.items():
        reversed_dict[value] = key  # Set the value as the new key and the key as the new value
    
    return reversed_dict  # Return the new reversed dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}  
print(reverse_dict(my_dict))  # Output: {1: 'a', 2: 'b', 3: 'c'}
