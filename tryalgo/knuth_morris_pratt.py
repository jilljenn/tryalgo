#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Find the length of maximal borders by Knuth-Morris-Pratt

jill-jênn vie, christoph dürr et louis abraham - 2014-2019
inspired from a practical lesson (TP) from Yves Lemaire
"""
# pylint: disable=undefined-variable, unused-argument


# snip{ maximum_border_length
def maximum_border_length(w):
    """Maximum string borders by Knuth-Morris-Pratt

    :param w: string
    :returns: table f such that f[i] is the longest border length of w[:i + 1]
    :complexity: linear
    """
    n = len(w)
    f = [0] * n                # init f[0] = 0
    k = 0                      # current longest border length
    for i in range(1, n):      # compute f[i]
        while w[k] != w[i] and k > 0:
            k = f[k - 1]       # mismatch: try the next border
        if w[k] == w[i]:       # last characters match
            k += 1             # we can increment the border length
        f[i] = k               # we found the maximal border of w[:i + 1]
    return f
# snip}


# snip{ knuth_morris_pratt
def knuth_morris_pratt(s, t):
    """Find a substring by Knuth-Morris-Pratt

    :param s: the haystack string
    :param t: the needle string
    :returns: index i such that s[i: i + len(t)] == t, or -1
    :complexity: O(len(s) + len(t))
    """
    sep = '\x00'                   # special unused character
    assert sep not in t and sep not in s
    f = maximum_border_length(t + sep + s)
    n = len(t)
    for i, fi in enumerate(f):
        if fi == n:                # found a border of the length of t
            return i - 2 * n       # beginning of the border in s
    return -1
# snip}


# snip{ powerstring_by_border
def powerstring_by_border(u):
    """Power string by Knuth-Morris-Pratt

    :param u: string
    :returns: largest k such that there is a string y with u = y^k
    :complexity: O(len(u))
    """
    f = maximum_border_length(u)
    n = len(u)
    if n % (n - f[-1]) == 0:       # does the alignment shift divide n ?
        return n // (n - f[-1])    # we found a power decomposition
    return 1
# snip}


# snip{ powerstring_by_find
def powerstring_by_find(u):
    """Power string using the python find method

    :param u: string
    :returns: largest k such that there is a string y with u = y^k
    :complexity: O(len(u)^2), this is due to the naive implementation of string.find
    """
    return len(u) // (u + u).find(u, 1)
# snip}
