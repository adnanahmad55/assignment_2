def fibonacciseq(n):
    if n <= 0:  # Handle invalid input
        print("Invalid input! n should be greater than 0.")
        return
    
    a, b = 0, 1  # Initialize first two terms
    
    print(a)  # Print first Fibonacci number
    if n > 1:
        print(b)  # Print second Fibonacci number
    
    for i in range(2, n):  # Generate remaining terms
        next1 = a + b
        print(next1)
        a, b = b, next1  # Move forward in the sequence

# Example usage
fibonacciseq(4)
