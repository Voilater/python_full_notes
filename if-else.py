
x = 10

if x > 5:
    print("x is greater than 5")


### `if`-`else` Statement


x = 4

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


### `if`-`elif`-`else` Statement

x = 8

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")


### Nested `if` Statements

x = 15

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is not greater than 20")
else:
    print("x is 10 or less")


### Logical Operators in Conditions

x = 7
y = 10

# Using 'and'
if x > 5 and y > 5:
    print("Both x and y are greater than 5")

# Using 'or'
if x > 5 or y > 5:
    print("At least one of x or y is greater than 5")

# Using 'not'
if not x > 10:
    print("x is not greater than 10")


### Inline `if`-`else` (Ternary Operator)

x = 10

# Traditional if-else
if x > 5:
    result = "Greater"
else:
    result = "Smaller or equal"

# Ternary operator
result = "Greater" if x > 5 else "Smaller or equal"

print(result)


### Examples

#### Example 1: Check if a number is positive, negative, or zero


num = 0

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")


#### Example 2: Determine the grade based on a score


score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")


### Using `if` with `in`


fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list of fruits")

if "orange" not in fruits:
    print("Orange is not in the list of fruits")


### Using `if` with Functions


def check_age(age):
    if age < 18:
        return "You are a minor"
    elif age < 65:
        return "You are an adult"
    else:
        return "You are a senior"

print(check_age(20))  # "You are an adult"
print(check_age(70))  # "You are a senior"

