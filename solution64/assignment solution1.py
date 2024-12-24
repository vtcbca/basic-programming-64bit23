from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial_reduce(n)}")