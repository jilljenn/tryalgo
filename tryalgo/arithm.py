#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
arithmetic functions

christoph dürr - jill-jênn vie - 2013-2019
"""
# pylint: disable=anomalous-backslash-in-string


# icpc-ignore
# snip{ pgcd
def pgcd(a, b):
    """Greatest common divisor for a and b

    :param a,b: non-negative integers
    :complexity: O(log a + log b)
    """
    return a if b == 0 else pgcd(b, a % b)
# snip}


# icpc-title Bezout
# snip{ bezout
def bezout(a, b):
    """Bézout coefficients for a and b

    :param a,b: non-negative integers
    :complexity: O(log a + log b)
    """
    if b == 0:
        return (1, 0)
    u, v = bezout(b, a % b)
    return (v, u - (a // b) * v)
# snip}


# icpc-ignore
# snip{
def inv(a, p):
    """Inverse of a in :math:`{mathbb Z}_p`

    :param a,p: non-negative integers
    :complexity: O(log a + log p)
    """
    return bezout(a, p)[0] % p
# snip}


# icpc-ignore
# snip{ binom
def binom(n, k):
    """Binomial coefficients for :math:`n choose k`

    :param n,k: non-negative integers
    :complexity: O(k)
    """
    prod = 1
    for i in range(k):
        prod = (prod * (n - i)) // (i + 1)
    return prod
# snip}


# icpc-ignore
# snip{ binom_modulo
def binom_modulo(n, k, p):
    """Binomial coefficients for :math:`n choose k`, modulo p

    :param n,k: non-negative integers
    :complexity: O(k)
    """
    prod = 1
    for i in range(k):
        prod = (prod * (n - i) * inv(i + 1, p)) % p
    return prod
# snip}

import math
a = b = n = k = 10
q = 19
# snip{
pow(a, b, q)        # fast_exponentiation
pow(a, -1, q)       # inv(a, q), Python >= 3.8
math.gcd(a, b)      # pgcd
math.comb(n, k)     # binom
# snip}