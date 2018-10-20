#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Levenshtein edit distance
# jill-jenn vie et christoph durr - 2014-2018


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
    #                         initializing row 0 and column 0
    A = [[i + j for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            A[i + 1][j + 1] = min(A[i][j + 1] + 1,              # insert
                                  A[i + 1][j] + 1,              # delete
                                  A[i][j] + int(x[i] != y[j]))  # subst.
    return A[n][m]
# snip}
