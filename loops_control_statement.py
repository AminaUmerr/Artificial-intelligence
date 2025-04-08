# Loop Control Statements

# Using 'continue' to skip specific iterations
i = 0
for i in range(10):
    if(i == 3):
        continue # ignore / skip specific statement
    print(i)

# Using 'break' to stop the loop
i = 0
for i in range(100):
    if(i == 33):
        break #break the loop
    print(i)

# Extra Example: Using 'pass' (does nothing but required syntactically)
for letter in "geeksforgeeks":
    if letter == "e":
        pass  # Placeholder for future code
    print("Processing:", letter)
