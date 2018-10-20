#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Permutation rank
# christoph durr - 2016-2018


def permutation_rank(p):
    """Given a permutation of {0,..,n-1} find its rank according to lexicographical order

       :param p: list of length n containing all integers from 0 to n-1
       :returns: rank between 0 and n! -1
       :beware: computation with big numbers
       :complexity: `O(n^2)`
    """
    n = len(p)
    fact = 1                                 # compute (n-1) factorial
    for i in range(2, n):
        fact *= i
    r = 0                                    # compute rank of p
    digits = list(range(n))                  # all yet unused digits
    for i in range(n-1):                     # for all digits except last one
        q = digits.index(p[i])
        r += fact * q
        del digits[q]                        # remove this digit p[i]
        fact //= (n - 1 - i)                 # weight of next digit
    return r


def rank_permutation(r, n):
    """Given r and n find the permutation of {0,..,n-1} with rank according to lexicographical order equal to r

       :param r n: integers with 0 ≤ r < n!
       :returns: permutation p as a list of n integers
       :beware: computation with big numbers
       :complexity: `O(n^2)`
    """
    fact = 1                                # compute (n-1) factorial
    for i in range(2, n):
        fact *= i
    digits = list(range(n))                 # all yet unused digits
    p = []                                  # build permutation
    for i in range(n):
        q = r // fact                       # by decomposing r = q * fact + rest
        r %= fact
        p.append(digits[q])
        del digits[q]                       # remove digit at position q
        if i != n - 1:
            fact //= (n - 1 - i)            # weight of next digit
    return p
