# DATA TYPES AND TYPE CONVERSION IN PYTHON
# The `type()` function tells you what kind of data a variable holds.
# Python supports different data types like numbers, booleans, and complex numbers.

print("\nShowing variable values and their data types:\n")

# 1. NUMBERS
# Python works with whole numbers, decimal numbers, and complex numbers.

# Whole numbers (integers)
num1 = 10
print("Number 1:", num1, "| Type:", type(num1))  # Output: Number 1: 10 | Type: <class 'int'>

num2 = -5
print("Number 2:", num2, "| Type:", type(num2))  # Output: Number 2: -5 | Type: <class 'int'>

# Decimal numbers (floats)
decimal1 = 3.14
print("Decimal 1:", decimal1, "| Type:", type(decimal1))  # Output: Decimal 1: 3.14 | Type: <class 'float'>

decimal2 = 2.5e3  # 2.5 × 1000 = 2500.0
print("Decimal 2:", decimal2, "| Type:", type(decimal2))  # Output: Decimal 2: 2500.0 | Type: <class 'float'>

# Complex numbers (with real and imaginary parts)
complex1 = 4 + 3j
print("Complex 1:", complex1, "| Type:", type(complex1))  # Output: Complex 1: (4+3j) | Type: <class 'complex'>

complex2 = -2j
print("Complex 2:", complex2, "| Type:", type(complex2))  # Output: Complex 2: (-0-2j) | Type: <class 'complex'>

# 2. BOOLEANS
# Booleans are used for True or False values.

bool1 = True
print("Boolean 1:", bool1, "| Type:", type(bool1))  # Output: Boolean 1: True | Type: <class 'bool'>

bool2 = False
print("Boolean 2:", bool2, "| Type:", type(bool2))  # Output: Boolean 2: False | Type: <class 'bool'>

# Boolean expressions (checking conditions)
check1 = (10 > 5)  # True, because 10 is greater than 5
print("Check 1:", check1, "| Type:", type(check1))  # Output: Check 1: True | Type: <class 'bool'>

check2 = (10 == 5)  # False, because 10 is not equal to 5
print("Check 2:", check2, "| Type:", type(check2))  # Output: Check 2: False | Type: <class 'bool'>

# Converting values to Booleans
convert1 = bool(0)  # 0 becomes False
print("Convert 1 (from 0):", convert1, "| Type:", type(convert1))  # Output: Convert 1 (from 0): False | Type: <class 'bool'>

convert2 = bool(10)  # Any non-zero number becomes True
print("Convert 2 (from 10):", convert2, "| Type:", type(convert2))  # Output: Convert 2 (from 10): True | Type: <class 'bool'>

convert3 = bool("")  # Empty string becomes False
print("Convert 3 (from empty string):", convert3, "| Type:", type(convert3))  # Output: Convert 3 (from empty string): False | Type: <class 'bool'>

convert4 = bool("Hello")  # Non-empty string becomes True
print("Convert 4 (from 'Hello'):", convert4, "| Type:", type(convert4))  # Output: Convert 4 (from 'Hello'): True | Type: <class 'bool'>
