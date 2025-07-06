#write python operators in python as per geeks for geeks
# Python Operators
# Arithmetic Operators
def arithmetic_operators(): 
    a = 10
    b = 20
    print("a + b =", a + b)  # Addition
    print("a - b =", a - b)  # Subtraction
    print("a * b =", a * b)  # Multiplication
    print("a / b =", a / b)  # Division
    print("a % b =", a % b)  # Modulus
    print("a ** b =", a ** b)  # Exponentiation
    print("a // b =", a // b)  # Floor Division

# Comparison Operators
def comparison_operators():
    a = 10
    b = 20
    print("a == b:", a == b)  # Equal to
    print("a != b:", a != b)  # Not equal to
    print("a > b:", a > b)    # Greater than
    print("a < b:", a < b)    # Less than
    print("a >= b:", a >= b)  # Greater than or equal to
    print("a <= b:", a <= b)  # Less than or equal to   

# Assignment Operators
def assignment_operators():
    a = 10
    print("a =", a)  # Assign
    a += 5
    print("a += 5:", a)  # Add and assign
    a -= 3
    print("a -= 3:", a)  # Subtract and assign
    a *= 2
    print("a *= 2:", a)  # Multiply and assign
    a /= 4
    print("a /= 4:", a)  # Divide and assign
    a %= 3
    print("a %= 3:", a)  # Modulus and assign
    a **= 2
    print("a **= 2:", a)  # Exponentiation and assign   

# Logical Operators
def logical_operators():
    a = True
    b = False
    print("a and b:", a and b)  # Logical AND
    print("a or b:", a or b)    # Logical OR
    print("not a:", not a)      # Logical NOT       
# Bitwise Operators
def bitwise_operators():
    a = 10  # 1010 in binary
    b = 4   # 0100 in binary
    print("a & b:", a & b)  # Bitwise AND
    print("a | b:", a | b)  # Bitwise OR
    print("a ^ b:", a ^ b)  # Bitwise XOR
    print("~a:", ~a)        # Bitwise NOT
    print("a << 2:", a << 2)  # Left Shift
    print("a >> 2:", a >> 2)  # Right Shift
# Identity Operators
def identity_operators():
    a = [1, 2, 3]
    b = a
    c = a[:]
    print("a is b:", a is b)  # True, same object
    print("a is c:", a is c)  # False, different objects
    print("a is not b:", a is not b)  # False
    print("a is not c:", a is not c)  # True
# Membership Operators
def membership_operators():
    a = [1, 2, 3, 4, 5]
    print("2 in a:", 2 in a)  # True
    print("6 not in a:", 6 not in a)  # True
    print("a[0] in a:", a[0] in a)  # True
# None Operator
def none_operator():
    a = None
    print("a is None:", a is None)  # True
    print("a is not None:", a is not None)  # False
# Main function to demonstrate all operators
def main():
    print("Arithmetic Operators:")
    arithmetic_operators()
    
    print("\nComparison Operators:")
    comparison_operators()
    
    print("\nAssignment Operators:")
    assignment_operators()
    
    print("\nLogical Operators:")
    logical_operators()
    
    print("\nBitwise Operators:")
    bitwise_operators()
    
    print("\nIdentity Operators:")
    identity_operators()
    
    print("\nMembership Operators:")
    membership_operators()
    
    print("\nNone Operator:")
    none_operator()