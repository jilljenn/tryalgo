#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maximum string borders by Knuth-Morris-Pratt
# jill-jênn vie et christoph dürr - 2014-2015

# part d'un TP de Yves Lemaire
# en temps linéaire avec Knuth-Morris-Pratt


# détermine la longueur des bords maximaux de u en temps linéaire.

# snip{
def maximum_border_length(w):
    """Maximum string borders by Knuth-Morris-Pratt

    :param w: string
    :returns: table l such that l[i] is the longest border length of w[:i + 1]
    :complexity: linear
    """
    n = len(w)
    L = [0] * (n + 1)
    for i in range(1, n):
        k = L[i]
        while w[k] != w[i] and k > 0:
            k = L[k]
        if w[k] == w[i]:
            L[i + 1] = k + 1
        else:
            L[i + 1] = 0
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

