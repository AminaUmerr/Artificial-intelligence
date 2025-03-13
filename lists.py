# LISTS IN PYTHON
# A list is a collection of elements enclosed within square brackets [].
# Lists can store multiple data types.

# Creating lists with various data types
numbers = [10, 20, 30, 40]  # List of integers
print(numbers)
print(type(numbers))

fruits = ["apple", "Mango", "cherry"]  # List of strings
print(fruits)
print(type(fruits))

mixed_list = [3.14, "Python", 100]  # List with mixed data types
print(mixed_list)
print(type(mixed_list))

# CREATING AN EMPTY LIST
empty = []
print("Empty List:", empty)

# ACCESSING LIST ELEMENTS USING INDICES
# List indexing starts from 0 in Python
shades = ["Cyan", "Magenta", "Yellow", "White"]

print("First Shade:", shades[0])   # Accessing the first item
print("Last Shade:", shades[-1])   # Accessing the last item
print("Subset of Shades:", shades[1:3])  # Extracting a portion of the list

# AVOIDING INDEX OUT OF RANGE ERROR
# Uncommenting the line below will cause an error
# print(shades[4])

# LIST SLICING
# Retrieving portions of the list
print("First two elements:", shades[:2])   # First two elements
print("From second to last:", shades[1:])  # Elements from index 1 onward
print("All except the last:", shades[:-1])  # Everything except the last element

# CONDITIONAL STATEMENTS IN PYTHON
# Conditional statements help in decision-making based on conditions.

x = 7
y = 15

if x == y:
    print("x and y are equal")
elif x < y:
    print("x is smaller than y")
else:
    print("x is larger than y")
