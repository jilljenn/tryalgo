#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Prime numbers by Eratosthene
# nombre premiers <n
# jill-jenn vie et christoph durr - 2014-2015


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
    This algorithm has better theoretical complexity as the sieve of Eratosthene, but is worse in practice

    :param n: positive integer
    :assumes: n > 2
    :returns: list of prime numbers <n
    :complexity: O(n)
    """
    succ = [i + 1 for i in range(n)]
    prec = [i - 1 for i in range(n)] 
    succ[n - 1] = 2
    prec[2] = n - 1
    p = 2
    while p * p < n:
        q = p
        while p * q < n:
            x = p * q
            while x < n:
                # remove the non prime x
                succ[prec[x]] = succ[x]
                prec[succ[x]] = prec[x]
                x *= p
            q = succ[q]
        p = succ[p]
    answ = [2]
    p = succ[2]
    while p != 2:
        answ.append(p)
        p = succ[p]
    return answ
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
