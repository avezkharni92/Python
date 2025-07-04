
def print_func():#Print Function 
    print("Hello Avez")
    #print_func()


def input_output(): #getting input from user and then printing
    name = input("What's your name:")
    print("Hello",name,"Nice to meet you:)")
    #input_output()


def type_casting():#By default the input Function takes as string
    #To convert it to other data type convert it using TypeCasting
    name = input("What's your name:")
    age = int(input("What's your age:"))
    print("Hello",name,"Nice to meet you:). You are",age,"Years Old")
    #Like doing some operation based on that
    print("In 5 Years you will be", age + 5,"Years old")
    #type_casting()


def multiple_input():#taking Multiple inputs as Variable
    x, y = input("Enter 2 Variables").split()
    print("Number of Boys is:",x,"and Number of girls is",y)

    #multiple_input()    


def find_data_types():#Find DataType of Input in Python
    a = "Hello World"
    b = 10
    c = 11.22
    d = ("Geeks", "for", "Geeks")
    e = ["Geeks", "for", "Geeks"]
    f = {"Geeks": 1, "for":2, "Geeks":3}


    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))

    #find_data_types()

# Output Formatting
# Output formatting in Python with various techniques including the format() method, 
# manipulation of the sep and end parameters, f-strings and the versatile % operator. 
# These methods enable precise control over how data is displayed, enhancing the readability and 
# effectiveness of your Python programs.
def format_operator_1():
    amount = 150.75
    print("Amount: ${:.2f}".format(amount))

    #format_operator_1()


def sep_operator_2(): #Output Formatting using sep and end operator

    #formatting : Python Sep(separator) operator in print
    #By default, the sep parameter is set to a space character, 
    #so if you don't specify it explicitly, the values will be separated by a space.
    x, y, z, a = input("Enter 4 values").split()
    print(x,y,z,a, sep='')
    print(x,y,z,a, sep="<>")

    #sep_operator()

    # Time Complexity:
    # The time complexity of the print() function is O(n), where n is the total number of characters to be printed. 
    # However, the time complexity of specifying a separator is O(1), as it is a constant time operation.

    # Space Complexity:
    # The space complexity of the code is also O(n), where n is the total number of characters to be printed. 
    # This is because the print() function needs to allocate memory to store the strings and separators before printing them out.
    # Overall, the code has a constant time complexity for specifying the separator, 
    # and a linear time and space complexity for printing out the strings and separators.


def end_operator_2():
    # end Parameter with '@'
    print("Python", end='@')
    print("GeeksforGeeks")

    #end_operator_2()


def f_string_3():
    # f-strings (formatted string literals) are a way to embed expressions inside string literals, 
    # using curly braces {}. They were introduced in Python 3.6 and provide a concise and readable way to format strings.
    name = "Avez"
    age = 20
    print(f"Hello {name}, you are {age} years old.")
    
    #f_string_3()


#Input and out[ut in python
def input_output_4():
    # Input and Output in Python
    # Python provides built-in functions for input and output operations.
    # The input() function is used to take input from the user, 
    # while the print() function is used to display output on the console.

    # Taking input from the user
    user_input = input("Enter something: ")
    print(f"You entered: {user_input}")

    # Output formatting using f-strings
    name = "Avez"
    age = 20
    print(f"Hello {name}, you are {age} years old.")

    #input_output_4()

def main():
    # print_func()
    # input_output()
    # type_casting()
    # multiple_input()
    # find_data_types()
    # format_operator_1()
    # sep_operator_2()
    # end_operator_2()
    # f_string_3()
    # input_output_4()
    pass