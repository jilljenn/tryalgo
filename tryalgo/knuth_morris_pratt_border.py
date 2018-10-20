#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum string borders by Knuth-Morris-Pratt
# jill-jênn vie et christoph dürr et louis abraham - 2014-2018
# inspired from a practical lesson (TP) from Yves Lemaire
# in linear time with Knuth-Morris-Pratt


# Find the length of maximal borders of u in linear time.

# snip{
def maximum_border_length(w):
    """Maximum string borders by Knuth-Morris-Pratt

    :param w: string
    :returns: table l such that l[i] is the longest border length of w[:i + 1]
    :complexity: linear
    """
    n = len(w)
    L = [0] * n
    k = 0
    for i in range(1, n):
        while w[k] != w[i] and k > 0:
            k = L[k - 1]
        if w[k] == w[i]:
            k += 1
            L[i] = k
        else:
            L[i] = 0
    return L
# snip}


# snip{ powerstring_by_border
def powerstring_by_border(u):
    """Power string by Knuth-Morris-Pratt

    :param x: string
    :returns: largest k such that there is a string y with x = y^k
    :complexity: O(len(x))
    """
    L = maximum_border_length(u)
    n = len(u)
    if n % (n - L[-1]) == 0:
        return n // (n - L[-1])
    return 1
# snip}
