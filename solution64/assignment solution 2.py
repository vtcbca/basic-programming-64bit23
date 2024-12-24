def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, limit + 1, start):
                sieve[i] = False
    return sieve

def is_prime_sieve(n):
    sieve = sieve_of_eratosthenes(n)
    return sieve[n]

n = int(input("Enter a number: "))
print(f"Is {n} prime? {is_prime_sieve(n)}")