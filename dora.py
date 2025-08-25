def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get user input
terms = int(input("Enter the number of Fibonacci terms: "))

# Print the sequence
print("Fibonacci sequence:", fibonacci(terms))
