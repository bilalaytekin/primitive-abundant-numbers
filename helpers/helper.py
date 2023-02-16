import math

def sieve_of_Eratosthenes(X):
    # This bitmap starts as false for 0 and 1, true for every 2 <= n <= X.
    primes_bitmap = [i > 1 for i in range(0, X + 1)]

    p = 2 # the first prime
    while p <= math.sqrt(X + 1):
        if primes_bitmap[p]:
            for i in range(p * p, X + 1, p):
                primes_bitmap[i] = False
        p += 1
    return [i for i in range(2, X + 1) if primes_bitmap[i]]