#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Levenshtein edit distance
# jill-jenn vie et christoph durr - 2014-2015


# snip{
def levenshtein(x, y):
    """Levenshtein edit distance

    :param x:
    :param y: strings
    :returns: distance
    :complexity: `O(|x|*|y|)`
    """
    n = len(x)
    m = len(y)
    #                         initialisation ligne 0 et colonne 0
    A = [[i + j for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            A[i + 1][j + 1] = min(A[i][j + 1] + 1,              # insertion
                                  A[i + 1][j] + 1,              # suppress.
                                  A[i][j] + int(x[i] != y[j]))  # substitut.
    return A[n][m]
# snip}
