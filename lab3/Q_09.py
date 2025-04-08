def fibonacci_series(limit):
    a = 1  # First number in Fibonacci series
    b = 1  # Second number in Fibonacci series
    
    # Continue printing numbers while 'a' is less than or equal to the limit
    while a <= limit:
        print(a, end=" ")  
        temp = a '
        a = b  
        b = temp + b  

fibonacci_series(50)  # Call the function with limit 50
