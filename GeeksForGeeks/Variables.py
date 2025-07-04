# Variables in Python are used to store data values.
## In Python, variables do not need to be declared with a specific data type,
# as Python is dynamically typed. This means that the type of a variable is determined at runtime   
# based on the value assigned to it. However, you can use the `type()` function to check the data type of a variable.
def variable_declaration():
    # Variable Declaration
    x = 5
    y = "Hello, World!"
    z = 3.14

    print("x:", x, "Type:", type(x))
    print("y:", y, "Type:", type(y))
    print("z:", z, "Type:", type(z))

    # variable_declaration()

def variable_assignment():
    # Variable Assignment
    a = 10
    b = a  # Assigning the value of 'a' to 'b'
    c = "Python"

    print("a:", a, "b:", b, "c:", c)

    # variable_assignment() 

def variable_reassignment():   
    # Variable Reassignment
    x = 5
    print("Before reassignment, x:", x)
    x = 10  # Reassigning a new value to 'x'
    print("After reassignment, x:", x)

    # variable_reassignment()

def variable_scope():
    # Variable Scope
    def inner_function():
        local_var = "I am local to inner_function"
        print("Inner function:", local_var)

    global_var = "I am global"
    print("Global variable:", global_var)
    
    inner_function()
    
    # Uncommenting the next line will raise an error because local_var is not accessible here
    # print(local_var)

    # variable_scope()

def variable_type_check():
    # Variable Type Check
    a = 42
    b = 3.14
    c = "Hello"
    
    print("Type of a:", type(a))
    print("Type of b:", type(b))
    print("Type of c:", type(c))

    # variable_type_check()

def variable_operations(): 
    # Variable Operations
    x = 10
    y = 5
    
    sum_result = x + y
    product_result = x * y
    division_result = x / y
    
    print("Sum:", sum_result)
    print("Product:", product_result)
    print("Division:", division_result)

    # variable_operations()

def variable_deletion():
    # Variable Deletion
    x = 10
    print("Before deletion, x:", x)
    
    del x  # Deleting the variable 'x'
    
    # Uncommenting the next line will raise an error because 'x' is deleted
    # print("After deletion, x:", x)

    print("Variable 'x' has been deleted.")

    # variable_deletion()

def variable_examples():
    variable_declaration()
    variable_assignment()
    variable_reassignment()
    variable_scope()
    variable_type_check()
    variable_operations()
    variable_deletion()

if __name__ == "__main__":
    variable_examples()
    # Uncomment the function calls below to test individual functionalities
    variable_declaration()
    variable_assignment()
    variable_reassignment()
    variable_scope()
    variable_type_check()
    variable_operations()
    variable_deletion()
