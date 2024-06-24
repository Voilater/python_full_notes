

# Integer variable
x = 10

# Float variable
y = 3.14

# String variable
name = "Alice"

# Boolean variable
is_valid = True

# List variable
numbers = [1, 2, 3, 4, 5]

# Dictionary variable
person = {"name": "Bob", "age": 25}

#### Basic Usage


print("Hello, World!")  # Prints a string
print(x)  # Prints the value of variable x


#### Printing Multiple Values


print("The value of x is", x)
print("Name:", name, "Age:", person["age"])


#### String Formatting

##### Using `f-strings` (Python 3.6+)


print(f"The value of x is {x}")
print(f"Name: {name}, Age: {person['age']}")


##### Using the `str.format()` Method


print("The value of x is {}".format(x))
print("Name: {}, Age: {}".format(name, person["age"]))


##### Using Percent Formatting


print("The value of x is %d" % x)
print("Name: %s, Age: %d" % (name, person["age"]))



print("Hello", "World", sep="-")  # Output: Hello-World
print("Hello", end="!!!\n")  # Output: Hello!!!


#### Printing Without a Newline


print("Hello", end=" ")
print("World")  # Output: Hello World


### Variable Methods

#### String Methods


s = "hello world"

# Convert to upper case
print(s.upper())  # "HELLO WORLD"

# Convert to lower case
print(s.lower())  # "hello world"

# Capitalize the first letter
print(s.capitalize())  # "Hello world"

# Title case
print(s.title())  # "Hello World"

# Replace a substring
print(s.replace("world", "there"))  # "hello there"

# Find a substring
print(s.find("world"))  # 6

# Check if the string starts with a substring
print(s.startswith("hello"))  # True

# Check if the string ends with a substring
print(s.endswith("world"))  # True

# Split the string into a list
print(s.split())  # ['hello', 'world']


### Arithmetic Operators


a = 10
b = 3

# Addition
print(a + b)  # 13

# Subtraction
print(a - b)  # 7

# Multiplication
print(a * b)  # 30

# Division (float)
print(a / b)  # 3.3333333333333335

# Division (integer)
print(a // b)  # 3

# Modulus (remainder)
print(a % b)  # 1

# Exponentiation
print(a ** b)  # 1000


### Comparison Operators


x = 5
y = 10

# Equal to
print(x == y)  # False

# Not equal to
print(x != y)  # True

# Greater than
print(x > y)  # False

# Less than
print(x < y)  # True

# Greater than or equal to
print(x >= y)  # False

# Less than or equal to
print(x <= y)  # True


### Logical Operators


x = True
y = False

# Logical AND
print(x and y)  # False

# Logical OR
print(x or y)  # True

# Logical NOT
print(not x)  # False


### Bitwise Operators


a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101

# Bitwise AND
print(a & b)  # 12 (0000 1100)

# Bitwise OR
print(a | b)  # 61 (0011 1101)

# Bitwise XOR
print(a ^ b)  # 49 (0011 0001)

# Bitwise NOT
print(~a)  # -61 (1100 0011)

# Bitwise left shift
print(a << 2)  # 240 (1111 0000)

# Bitwise right shift
print(a >> 2)  # 15 (0000 1111)


### Assignment Operators

a = 10

# Simple assignment
a = 5
print(a)  # 5

# Add and assign
a += 2
print(a)  # 7

# Subtract and assign
a -= 3
print(a)  # 4

# Multiply and assign
a *= 2
print(a)  # 8

# Divide and assign (float)
a /= 4
print(a)  # 2.0

# Divide and assign (integer)
a //= 2
print(a)  # 1.0

# Modulus and assign
a %= 2
print(a)  # 1.0

# Exponentiate and assign
a **= 3
print(a)  # 1.0

# Bitwise AND and assign
a = 5
a &= 3
print(a)  # 1

# Bitwise OR and assign
a |= 2
print(a)  # 3

# Bitwise XOR and assign
a ^= 1
print(a)  # 2

# Bitwise left shift and assign
a <<= 1
print(a)  # 4

# Bitwise right shift and assign
a >>= 2
print(a)  # 1


### Membership Operators


my_list = [1, 2, 3, 4, 5]

# In
print(3 in my_list)  # True

# Not in
print(6 not in my_list)  # True


### Identity Operators


x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Is
print(x is z)  # True (z is the same object as x)
print(x is y)  # False (y is a different object with the same content)

# Is not
print(x is not y)  # True
print(x is not z)  # False


### Operator Precedence


result = 10 + 2 * 3  # 10 + 6 = 16 (multiplication has higher precedence than addition)
print(result)

# Using parentheses to change the order of evaluation
result = (10 + 2) * 3  # 12 * 3 = 36
print(result)

