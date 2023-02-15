import math
import sys

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
                    kind = classify(n, A[n][1])
                    if kind == 'abundant' or kind == 'perfect':
                        for i in range(2 * n, X + 1, n):
                            pan_bitmap[i] = False
                    if kind == 'perfect' or kind == 'deficient':
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

def classify(n, prime_factorization):
    assert is_factorization_correct(n, prime_factorization)
    tau = 1
    for (p, e) in prime_factorization:
        tau *= (p**(e+1) - 1) / (p - 1)
    if tau > 2 * n:
        return 'abundant'
    elif tau == 2 * n:
        return 'perfect'
    else:
        return 'deficient'

def is_factorization_correct(n, prime_factorization):
    m = 1
    for (p, e) in prime_factorization:
        m *= p ** e
    return n == m

X = int(sys.argv[1])
pans = sift_PANs_up_to(X)
file = open('pans_up_to_%s.txt' % X,'w')
for pan in pans:
	file.write('%s\n' % pan)
file.close()
