#In Python, decision-making statements manage the program's flow depending on specified conditions.
#The if statement executes a block of code when the condition evaluates to true, whereas if-else 
#offers an alternate route. The if-elif-else construct evaluates multiple conditions and runs the 
#first one that holds true. Correct indentation is crucial to ensure proper execution.

# 1. If statement  
num = 12  
if num > 8:  
    print("The number is greater than 5")  

# 2. If-else statement  
age = 15 
if age >= 15:  
    print("You are an adult")  
else:  
    print("You are a minor")  

# 3. If-else if-else statement  
num = 15
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

