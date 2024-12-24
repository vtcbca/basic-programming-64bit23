def fibonacci_max_value(max_val):
    fib_sequence = []
    a, b = 0, 1
    while a <= max_val:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

max_val = int(input("Enter the maximum value: "))
print(f"Fibonacci sequence up to {max_val}: {fibonacci_max_value(max_val)}")