# Based on this you can learn about Python operators.
# Python Operators
# Python supports the following types of operators:
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Assignment Operators
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Identity Operators
# 7. Membership Operators       
# 8. Special Operators  
# 9. Ternary Operator
# 10. Lambda Operator
# 11. Operator Overloading
# 12. Augmented Assignment Operators
# 13. Chained Assignment Operators
# 14. In-place Operators
# 15. Short-circuit Evaluation Operators
# 16. Operator Precedence and Associativity
# 17. Operator Functions            
# 18. Operator Overloading with Magic Methods
# 19. Operator Overloading with Decorators
# 20. Operator Overloading with Class Methods
# 21. Operator Overloading with Static Methods
# 22. Operator Overloading with Class Variables
# 23. Operator Overloading with Class Properties
# 24. Operator Overloading with Class Inheritance
# 25. Operator Overloading with Class Composition
# 26. Operator Overloading with Class Decorators
# 27. Operator Overloading with Class Context Managers
# 28. Operator Overloading with Class Metaclasses
# 29. Operator Overloading with Class Abstract Base Classes
# 30. Operator Overloading with Class Type Hints
# 31. Operator Overloading with Class Type Annotations
# 32. Operator Overloading with Class Type Checking
# 33. Operator Overloading with Class Type Casting
# 34. Operator Overloading with Class Type Conversion
# 35. Operator Overloading with Class Type Coercion

#Write a Python program to demonstrate the use of various operators.
# Arithmetic Operators
def arithmetic_operators():
    a = 10
    b = 5
    print("Arithmetic Operators:")
    print(f"a + b = {a + b}")  # Addition
    print(f"a - b = {a - b}")  # Subtraction
    print(f"a * b = {a * b}")  # Multiplication
    print(f"a / b = {a / b}")  # Division
    print(f"a % b = {a % b}")  # Modulus
    print(f"a ** b = {a ** b}")  # Exponentiation like 10*10*10*10*10 here
    print(f"a // b = {a // b}")  # Floor Division


# Comparison Operators
def comparison_operators():
    a = 10
    b = 5
    print("\nComparison Operators:")
    print(f"a == b: {a == b}")  # Equal to
    print(f"a != b: {a != b}")  # Not equal to
    print(f"a > b: {a > b}")    # Greater than
    print(f"a < b: {a < b}")    # Less than
    print(f"a >= b: {a >= b}")  # Greater than or equal to
    print(f"a <= b: {a <= b}")  # Less than or equal to

# Assignment Operators
def assignment_operators():
    a = 10
    print("\nAssignment Operators:")
    print(f"a = {a}")  # Assign
    a += 5
    print(f"a += 5: {a}")  # Add and assign
    a -= 3
    print(f"a -= 3: {a}")  # Subtract and assign
    a *= 2
    print(f"a *= 2: {a}")  # Multiply and assign
    a /= 4
    print(f"a /= 4: {a}")  # Divide and assign
    a %= 3
    print(f"a %= 3: {a}")  # Modulus and assign

# Logical Operators
def logical_operators():
    a = True
    b = False
    print("\nLogical Operators:")
    print(f"a and b: {a and b}")  # Logical AND
    print(f"a or b: {a or b}")    # Logical OR
    print(f"not a: {not a}")      # Logical NOT

# Bitwise Operators
def bitwise_operators():
    a = 10  # 1010 in binary
    b = 4   # 0100 in binary
    print("\nBitwise Operators:")
    print(f"a & b: {a & b}")  # Bitwise AND
    print(f"a | b: {a | b}")  # Bitwise OR
    print(f"a ^ b: {a ^ b}")  # Bitwise XOR
    print(f"~a: {~a}")        # Bitwise NOT
    print(f"a << 1: {a << 1}")  # Left shift
    print(f"a >> 1: {a >> 1}")  # Right shift   

# Identity Operators
def identity_operators():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print("\nIdentity Operators:")
    print(f"a is b: {a is b}")      # Identity check
    print(f"a is not c: {a is not c}")  # Identity check
    print(f"a is c: {a is c}")      # Identity check
    print(f"a == c: {a == c}")      # Equality check

# Membership Operators
def membership_operators():
    a = [1, 2, 3, 4, 5]
    print("\nMembership Operators:")
    print(f"2 in a: {2 in a}")      # Membership check
    print(f"6 not in a: {6 not in a}")  # Membership check

# Special Operators
def special_operators():
    a = 10
    b = 5
    print("\nSpecial Operators:")
    print(f"a // b: {a // b}")  # Floor Division
    print(f"a % b: {a % b}")    # Modulus
    print(f"a ** b: {a ** b}")  # Exponentiation

# Ternary Operator
def ternary_operator():
    a = 10
    b = 5
    print("\nTernary Operator:")
    result = "a is greater" if a > b else "b is greater"
    print(result)       

# Lambda Operator
def lambda_operator():
    add = lambda x, y: x + y
    print("\nLambda Operator:")
    print(f"add(10, 5) = {add(10, 5)}")  # Lambda function for addition 

# Operator Overloading
class Vector:           
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
def operator_overloading():
    v1 = Vector(2, 3)
    v2 = Vector(5, 7)
    print("\nOperator Overloading:")
    print(f"v1 + v2 = {v1 + v2}")  # Vector addition
    print(f"v1 - v2 = {v1 - v2}")  # Vector subtraction                         
# Augmented Assignment Operators
def augmented_assignment_operators():       
    a = 10
    print("\nAugmented Assignment Operators:")
    a += 5
    print(f"a += 5: {a}")  # Add and assign
    a -= 3
    print(f"a -= 3: {a}")  # Subtract and assign
    a *= 2
    print(f"a *= 2: {a}")  # Multiply and assign
    a /= 4
    print(f"a /= 4: {a}")  # Divide and assign
    a %= 3
    print(f"a %= 3: {a}")  # Modulus and assign 
# Chained Assignment Operators
def chained_assignment_operators():
    a = b = c = 10
    print("\nChained Assignment Operators:")
    print(f"a = {a}, b = {b}, c = {c}")  # Chained assignment
    a += 5
    print(f"After a += 5, a = {a}, b = {b}, c = {c}")  # Chained assignment after modification  

# In-place Operators
def in_place_operators():
    a = 10
    print("\nIn-place Operators:")
    a += 5
    print(f"a += 5: {a}")  # In-place addition
    a -= 3
    print(f"a -= 3: {a}")  # In-place subtraction
    a *= 2
    print(f"a *= 2: {a}")  # In-place multiplication
    a /= 4
    print(f"a /= 4: {a}")  # In-place division
    a %= 3
    print(f"a %= 3: {a}")  # In-place modulus

# Short-circuit Evaluation Operators
def short_circuit_evaluation_operators():
    a = True
    b = False
    print("\nShort-circuit Evaluation Operators:")
    print(f"a and b: {a and b}")  # Short-circuit AND
    print(f"a or b: {a or b}")    # Short-circuit OR
    print(f"not a: {not a}")      # Logical NOT 

# Operator Precedence and Associativity
def operator_precedence_and_associativity():
    a = 10
    b = 5
    c = 2
    print("\nOperator Precedence and Associativity:")
    result = a + b * c  # Multiplication has higher precedence than addition
    print(f"a + b * c = {result}")  # Result is 20 (5 * 2 = 10, then 10 + 10 = 20)
    result = (a + b) * c  # Parentheses change precedence
    print(f"(a + b) * c = {result}")  # Result is 30 (15 * 2 = 30)  

# Operator Functions        
def operator_functions():
    a = 10
    b = 5
    print("\nOperator Functions:")
    print(f"max(a, b) = {max(a, b)}")  # Maximum of a and b
    print(f"min(a, b) = {min(a, b)}")  # Minimum of a and b
    print(f"abs(-a) = {abs(-a)}")      # Absolute value of -a