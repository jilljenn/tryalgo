#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Prime numbers by Eratosthene
# nombre premiers <n
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def eratosthene(n):
    """Prime numbers by Eratosthene

    :param n: positive integer
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


