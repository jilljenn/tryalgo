#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# subsetsum
# jill-jenn vie et christoph durr - 2015-2018


# snip{ subsetsum
def subset_sum(x, R):
    """Subsetsum

    :param x: table of non negative values
    :param R: target value
    :returns bool: True if a subset of x sums to R
    :complexity: O(n*R)
    """
    b = [False] * (R + 1)
    b[0] = True
    for xi in x:
        for s in range(R, xi - 1, -1):
            b[s] |= b[s - xi]
    return b[R]
# snip}


# snip{ coinchange
def coin_change(x, R):
    """Coin change

    :param x: table of non negative values
    :param R: target value
    :returns bool: True if there is a non negative linear combination of x that has value R
    :complexity: O(n*R)
    """
    b = [False] * (R + 1)
    b[0] = True
    for xi in x:
        for s in range(xi, R + 1):
            b[s] |= b[s - xi]
    return b[R]
# snip}
