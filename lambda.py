### Example 1: Basic Lambda Function


# Lambda function to calculate the square of a number
square = lambda x: x ** 2

print(square(5))  # Output: 25


### Example 2: Lambda Function with Multiple Arguments


# Lambda function to add two numbers
add = lambda a, b: a + b

print(add(3, 4))  # Output: 7


### Example 3: Using Lambda with Built-in Functions

#### Using `map()` with Lambda


# Using map() with lambda to square each element in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # Output: [1, 4, 9, 16, 25]


#### Using `filter()` with Lambda


# Using filter() with lambda to filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]


#### Using `sorted()` with Lambda


# Using sorted() with lambda to sort a list of tuples by the second element
items = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_items = sorted(items, key=lambda x: x[1])

print(sorted_items)  # Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]

