import math

def sift_PANs_up_to(X):
    P = sieve_of_Eratosthenes(X)

    # This bitmap starts as false for 0 and 1, true for every 2 <= n <= X.
    pan_bitmap = [i > 1 for i in range(0, X + 1)]
    A = [[i, set()] for i in range(0, X + 1)]
    
    while P:
        p = P.pop(0)
        for n in range(p, X + 1, p):
            if pan_bitmap[n]:
                m = n
                e = 0
                while m % p == 0:
                    e += 1
                    m /= p
                A[n][0] = A[n][0]/(p ** e)
                A[n][1].add((p, e))
                if A[n][0] == 1:
                    if is_abundant(n, A[n][1]):
                        for i in range(2 * n, X + 1, n):
                            pan_bitmap[i] = False
                    else:
                        pan_bitmap[n] = False

    return [i for i in range(X + 1) if pan_bitmap[i]]

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

def is_abundant(n, prime_factorization):
    assert is_factorization_correct(n, prime_factorization)

    tau = 1
    for (p, e) in prime_factorization:
        tau *= (p**(e+1) - 1) / (p - 1)
    return tau > 2 * n

def is_factorization_correct(n, prime_factorization):
    m = 1
    for (p, e) in prime_factorization:
        m *= p ** e
    return n == m