# Function with list parameter
def print_items(items):
    for item in items:
        print(item)

groceries = ["orange", "grape", "kiwi"]
print_items(groceries)

# Extra Example: Function to calculate sum of list elements
def calculate_total(values):
    return sum(values)

print(calculate_total([10, 20, 30, 40, 50]))

print(sum([5, 10, 15]))


# Function with keyword arguments
def show_children(youngest, middle, eldest):
    print("The youngest child is " + youngest)

show_children(eldest="Emily", middle="Tom", youngest="Leo")

# Extra Example: Function with arbitrary keyword arguments
def display_details(details):
    for key, value in details.items():
        print(key, ":", value)

display_details(name="Alex", age=30, country="Canada")
