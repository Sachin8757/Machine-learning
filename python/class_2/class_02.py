# Syntax of variable assignment
a=1
b = 2
name="John Doe"
d=False
e=True
g=3.5
# print types of variables

print(type(a))  
print(type(b))
print(type(name))
print(type(d))
print(type(e))
print(type(g))
# Syntax of variable assignment with multiple variables
x, y, z = 1, 2, 3
# print values of multiple variables
print(x, y, z)

# operators 
# Arithmetic operators
print(1 + 2)  # Addition
print(5 - 3)  # Subtraction
print(4 * 2)  # Multiplication
print(8 / 2)  # Division
print(5 % 2)  # Modulus
print(2 ** 3) # Exponentiation
print(10 // 3) # Floor Division
# Comparison operators
print(5 == 5)  # Equal to
print(5 != 3)  # Not equal to
print(5 > 3)   # Greater than
print(5 < 3)   # Less than
print(5 >= 5)  # Greater than or equal to
print(5 <= 3)  # Less than or equal to
# Logical operators
print(True and False)  # Logical AND
print(True or False)   # Logical OR
print(not True)        # Logical NOT
# Bitwise operators
print(5 & 3)   # Bitwise AND
print(5 | 3)   # Bitwise OR
print(5 ^ 3)   # Bitwise XOR
print(~5)      # Bitwise NOT
print(5 << 1)  # Bitwise left shift
print(5 >> 1)  # Bitwise right shift
# Assignment operators
a = 5
a += 2  # Equivalent to a = a + 2   
print(a)  # Output: 7
a -= 3  # Equivalent to a = a - 3
print(a)  # Output: 4
a *= 2  # Equivalent to a = a * 2
print(a)  # Output: 8
a /= 4  # Equivalent to a = a / 4
print(a)  # Output: 2.0
a %= 2  # Equivalent to a = a % 2   
print(a)  # Output: 0.0
a **= 3  # Equivalent to a = a ** 3
print(a)  # Output: 0.0
a //= 1  # Equivalent to a = a // 1
print(a)  # Output: 0.0