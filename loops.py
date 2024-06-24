
#### Syntax


for item in iterable:
    # Execute block of code
    # Use 'item' inside the loop


#### Example 1: Iterate over a list


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


#Output:

apple
banana
cherry


#### Example 2: Iterate over a string


message = "Hello"

for char in message:
    print(char)


#Output:

H
e
l
l
o


#### Example 3: Iterate using range()


for i in range(5):
    print(i)


#Output:

0
1
2
3
4


### `while` Loop


#### Syntax


while condition:
    # Execute block of code
    # Condition should eventually become False to exit the loop


#### Example 1: Simple `while` loop


count = 0

while count < 5:
    print(count)
    count += 1


#Output:

0
1
2
3
4


#### Example 2: `while` loop with user input


while True:
    user_input = input("Enter a number (or 'quit' to exit): ")
    
    if user_input == 'quit':
        break  # Exit the loop
    
    num = int(user_input)
    print(f"Square of {num} is {num ** 2}")


### `break`, `continue`, and `else` in Loops


#### Example: Using `break` and `continue`


numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue  # Skip printing 3
    
    print(num)
    
    if num == 4:
        break  # Stop the loop when 4 is encountered
else:
    print("Loop completed normally")


#Output:

1
2
4


#### Example: Nested `for` loops


for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")


#Output:

(0, 0)
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)


#### Example: Nested `while` loop


i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(f"({i}, {j})")
        j += 1
    i += 1


#Output:

(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)


### Looping with `enumerate()`

#### Example: Using `enumerate()`


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


#Output:

# Index 0: apple
# Index 1: banana
# Index 2: cherry

