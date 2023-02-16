import os, sys, statistics
from helpers.helper import sieve_of_Eratosthenes
from sifting_abundant_numbers import PANs_up_to

def distributions_among_APs(N, pans=[], primes=[]):
    if primes==[]:
        primes = sieve_of_Eratosthenes(N)
    if pans==[]:
        if os.path.exists('./pans_up_to_%s.txt' % N):
            file = open('./pans_up_to_%s.txt' % 10000000, 'r')
            pans = []
            for pan in file.readlines():
                pans.append(int(pan))
        else:
            pans = PANs_up_to(N, primes)

    distributions = [[0 for i in range(p - 1)] for p in primes]
    for pan in pans:
        index = 0
        for p in primes:
            if pan % p != 0:
                distributions[index][pan % p - 1] += 1
            index += 1
    
    return distributions

def analyze_distributions(N, primes=[]):
    if primes==[]:
        primes = sieve_of_Eratosthenes(N)
    distributions = distributions_among_APs(N, primes=primes)
    mins = [min(distributions[i]) for i in range(len(primes))]
    maxs = [max(distributions[i]) for i in range(len(primes))]
    min_indexes = [distributions[i].index(mins[i]) + 1 for i in range(len(primes))]
    max_indexes = [distributions[i].index(maxs[i]) + 1 for i in range(len(primes))]
    ratios = [float(maxs[i])/float(mins[i]) for i in range(len(primes))]
    return distributions, mins, min_indexes, maxs, max_indexes, ratios