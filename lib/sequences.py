def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the specified length.
    
    Args:
        length: The number of Fibonacci numbers to generate
    
    Returns:
        A list containing the Fibonacci sequence
    """
    if length <= 0:
        print([])
        return []
    elif length == 1:
        result = [0]
        print(result)
        return result
    elif length == 2:
        result = [0, 1]
        print(result)
        return result
    
    # Start with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the rest of the sequence
    for i in range(2, length):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    print(fib_sequence)
    return fib_sequence