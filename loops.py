# Loops in Python

# While loop 
count = 0
while count < 5:
    count += 1
    print("Hello World")

# For loop with a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# For loop with a tuple
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# For loop with a string
print("\nString Iteration")
s = "World"
for i in s:
    print(i)

# Extra Example: Looping through a dictionary
print("\nDictionary Iteration")
d = {"name": "Amna", "age": 20}
for key, value in d.items():
    print(key, ":", value)
