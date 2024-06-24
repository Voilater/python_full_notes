
### Creating a List


# Empty list
my_list = []

# List with initial values
my_list = [1, 2, 3, 'apple', 'banana']


### Accessing List Items

# Access by index
print(my_list[0])  # First item
print(my_list[-1])  # Last item

# Slicing
print(my_list[1:3])  # Items from index 1 to 2


### Modifying Lists


# Change item
my_list[0] = 'orange'

# Add item
my_list.append('cherry')

# Insert item at a specific position
my_list.insert(1, 'grape')

# Remove item
my_list.remove('banana')

# Remove item at specific position
del my_list[1]

# Remove and return the last item
last_item = my_list.pop()

# Remove and return an item at a specific position
specific_item = my_list.pop(2)

# Clear the entire list
my_list.clear()



### Examples of List Methods


my_list = [3, 1, 4, 1, 5, 9, 2]

# Append
my_list.append(6)
print(my_list)  # [3, 1, 4, 1, 5, 9, 2, 6]

# Extend
my_list.extend([5, 3, 5])
print(my_list)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Insert
my_list.insert(2, 'new')
print(my_list)  # [3, 1, 'new', 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Remove
my_list.remove('new')
print(my_list)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Pop
item = my_list.pop()
print(item)  # 5
print(my_list)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Clear
my_list.clear()
print(my_list)  # []

# Index
my_list = [3, 1, 4, 1, 5, 9, 2]
print(my_list.index(4))  # 2

# Count
print(my_list.count(1))  # 2

# Sort
my_list.sort()
print(my_list)  # [1, 1, 2, 3, 4, 5, 9]

# Reverse
my_list.reverse()
print(my_list)  # [9, 5, 4, 3, 2, 1, 1]

# Copy
new_list = my_list.copy()
print(new_list)  # [9, 5, 4, 3, 2, 1, 1]



# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0][1])  # 2

# Using nested loops to iterate over a nested list
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()


### List Membership

my_list = [1, 2, 3, 4, 5]

print(3 in my_list)  # True
print(6 in my_list)  # False

#----------------------------------------------------------------------------
#### tuple
# Empty tuple
empty_tuple = ()

# Tuple with initial values
my_tuple = (1, 2, 3, 'apple', 'banana')

# Single element tuple (note the comma)
single_element_tuple = (5,)

# Access by index
print(my_tuple[0])  # First item
print(my_tuple[-1])  # Last item

# Slicing
print(my_tuple[1:3])  # Items from index 1 to 2

# Length of a tuple
print(len(my_tuple))  # 5

# Count occurrences of a value
print(my_tuple.count('apple'))  # 1

# Find the index of a value
print(my_tuple.index(3))  # 2

# Unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # 1 2 3 apple banana

# Unpacking with *
a, *b, c = my_tuple
print(a)  # 1
print(b)  # [2, 3, 'apple']
print(c)  # banana

nested_tuple = (1, 2, (3, 4), (5, (6, 7)))
print(nested_tuple[2][1])  # 4
print(nested_tuple[3][1][0])  # 6


#---------------------------------------------------------------------------------

# Empty set
empty_set = set()

# Set with initial values
my_set = {1, 2, 3, 'apple', 'banana'}

# Using the set() function
another_set = set([1, 2, 3, 'apple', 'banana'])

# Add an element
my_set.add('cherry')
print(my_set)  # {1, 2, 3, 'banana', 'cherry', 'apple'}

# Remove an element
my_set.remove('banana')
print(my_set)  # {1, 2, 3, 'cherry', 'apple'}

# Discard an element (does not raise an error if the element is not found)
my_set.discard('banana')

# Remove and return an arbitrary element
element = my_set.pop()
print(element)  # 1 (or any other element, since sets are unordered)

# Clear the set
my_set.clear()
print(my_set)  # set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # {1, 2, 4, 5}

# Check if a set is a subset of another
print(set1.issubset({1, 2, 3, 4}))  # True

# Check if a set is a superset of another
print(set1.issuperset({1, 2}))  # True

# Check if two sets are disjoint
print(set1.isdisjoint({4, 5, 6}))  # True

# Copy a set
copy_set = set1.copy()
print(copy_set)  # {1, 2, 3}

#---------------------------------------------------------------------------------
#### Dictionary Methods


person = {"name": "Alice", "age": 30}

# Get a value
print(person.get("name"))  # "Alice"

# Add a new key-value pair
person["city"] = "New York"
print(person)  # {"name": "Alice", "age": 30, "city": "New York"}

# Remove a key-value pair
del person["age"]
print(person)  # {"name": "Alice", "city": "New York"}

# Iterate over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Get all keys
keys = person.keys()
print(keys)  # dict_keys(['name', 'city'])

# Get all values
values = person.values()
print(values)  # dict_values(['Alice', 'New York'])

# Get all key-value pairs
items = person.items()
print(items)  # dict_items([('name', 'Alice'), ('city', 'New York')])

# Check if a key exists
print("name" in person)  # True

# Clear the dictionary
person.clear()
print(person)  # {}

