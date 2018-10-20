#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Prime numbers by Eratosthene
# nombre premiers <n
# jill-jenn vie et christoph durr - 2014-2018


# snip{ eratosthene
def eratosthene(n):
    """Prime numbers by sieve of Eratosthene

    :param n: positive integer
    :assumes: n > 2
    :returns: list of prime numbers <n
    :complexity: O(n loglog n)
    """
    P = [True] * n
    answ = [2]
    for i in range(3, n, 2):
        if P[i]:
            answ.append(i)
            for j in range(2 * i, n, i):
                P[j] = False
    return answ
# snip}


# snip{ gries_misra
def gries_misra(n):
    """Prime numbers by the sieve of Gries-Misra
    Computes both the list of all prime numbers less than n,
    and a table mapping every integer 2 ≤ x < n to its smallest prime factor

    :param n: positive integer
    :returns: list of prime numbers, and list of prime factors
    :complexity: O(n)
    """
    primes = []
    factor = [0] * n
    for x in range(2, n):
        if not factor[x]:     # no factor found
            factor[x] = x     # meaning x is prime
            primes.append(x)
        for p in primes:      # loop over all non primes of the form p * x
            if p > factor[x] or p * x >= n:
                break
            factor[p * x] = p
    return primes, factor
# snip}


if __name__ == "__main__":

    # compare the running times and show the ratio between the performances

    from time import time

    def test(f, n):
        start = time()
        for _ in range(10):
            f(n)
        return time() - start

    print("eratosthene\tgries_misra\tratio")
    n = 4
    for _ in range(30):
        E = test(eratosthene, n)
        G = test(gries_misra, n)
        print("%f\t%f\t%f" % (E, G, G / E) )
        n *= 2
